from flask import Flask, render_template, Response, request
from ultralytics import YOLO
import cv2
import os
import requests

app = Flask(__name__)

# URL do modelo YOLO hospedado no GitHub
MODEL_URL = "https://github.com/JLeoBRx/ReconhecendoEPIcomIA/raw/main/best.pt"
MODEL_PATH = "best.pt"

# Baixar o modelo do GitHub se não estiver presente
if not os.path.exists(MODEL_PATH):
    print("Baixando o modelo YOLO...")
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)
    print("Modelo baixado com sucesso!")

# Inicialize o modelo YOLO
model = YOLO(MODEL_PATH)

# Diretórios de saída
UPLOAD_FOLDER = "static/output"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Variável global para armazenar a fonte de entrada
video_source = 0


def generate_frames(source):
    """Gera frames processados para streaming."""
    cap = cv2.VideoCapture(source)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Processar os frames com YOLO
        results = model.predict(source=frame, conf=0.15, stream=True)
        for result in results:
            annotated_frame = result.plot()

        # Encode os frames em formato JPEG
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Enviar os frames para o cliente
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    """Endpoint para streaming de vídeo."""
    return Response(generate_frames(video_source),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/process", methods=["POST"])
def process():
    global video_source

    input_type = request.form.get("input_type")
    if input_type == "webcam":
        video_source = 0  # Webcam
        return render_template("stream.html", mode="webcam")

    elif input_type == "video":
        if "file" not in request.files:
            return "Nenhum arquivo selecionado!"
        file = request.files["file"]
        if file.filename == "":
            return "Nenhum arquivo escolhido!"
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        video_source = file_path  # Atualiza a fonte para o arquivo de vídeo
        return render_template("stream.html", mode="video")

    elif input_type == "image":
        if "file" not in request.files:
            return "Nenhum arquivo selecionado!"
        file = request.files["file"]
        if file.filename == "":
            return "Nenhum arquivo escolhido!"
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Processar a imagem
        results = model.predict(source=file_path, conf=0.15, save=True, project=UPLOAD_FOLDER, name="image_results")
        output_path = os.path.join(UPLOAD_FOLDER, "image_results", file.filename)
        return render_template("index.html", output_file=output_path)

    return "Opção inválida!"


if __name__ == "__main__":
    # Use app.run para rodar localmente ou durante testes
    app.run(debug=True)
