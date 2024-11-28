import sys
import os
import cv2
from PyQt5.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QPushButton, QFileDialog,
    QWidget, QMainWindow, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from ultralytics import YOLO

# Caminho absoluto para o modelo YOLO
MODEL_PATH = r"C:\yolo\best.pt"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reconhecendo EPI com IA")
        self.setGeometry(100, 100, 1024, 768)

        # Widget principal
        self.central_widget = MainWidget()
        self.setCentralWidget(self.central_widget)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout principal
        self.layout = QVBoxLayout()

        # Título
        self.title_label = QLabel("Reconhecendo EPI com IA")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #004080;")
        self.layout.addWidget(self.title_label)

        # Exibição da imagem ou vídeo (tamanho fixo)
        self.display_label = QLabel()
        self.display_label.setStyleSheet("border: 1px solid black; background-color: #d6eaff;")
        self.display_label.setFixedSize(640, 480)  # Define o tamanho fixo do QLabel
        self.display_label.setAlignment(Qt.AlignCenter)  # Centraliza o conteúdo
        self.layout.addWidget(self.display_label, alignment=Qt.AlignCenter)  # Centraliza o QLabel no layout

        # Combobox para selecionar o tipo de entrada
        self.input_selector = QComboBox()
        self.input_selector.addItems(["Imagem", "Vídeo", "Webcam"])
        self.layout.addWidget(self.input_selector, alignment=Qt.AlignCenter)

        # Botões
        self.button_layout = QHBoxLayout()

        self.upload_button = QPushButton("Escolher Arquivo")
        self.upload_button.clicked.connect(self.choose_file)
        self.button_layout.addWidget(self.upload_button)

        self.detect_button = QPushButton("Detectar")
        self.detect_button.clicked.connect(self.detect)
        self.detect_button.setEnabled(False)
        self.button_layout.addWidget(self.detect_button)

        self.layout.addLayout(self.button_layout)

        # Botão de sair
        self.exit_button = QPushButton("Sair")
        self.exit_button.clicked.connect(self.close_application)
        self.layout.addWidget(self.exit_button, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        # Variáveis para armazenar o caminho da entrada e status
        self.input_path = None
        self.cap = None
        self.timer = QTimer()

    def choose_file(self):
        # Tipo de entrada selecionado
        input_type = self.input_selector.currentText()

        if input_type == "Imagem":
            file_path, _ = QFileDialog.getOpenFileName(self, "Escolher Imagem", "", "Imagens (*.jpg *.jpeg *.png)")
        elif input_type == "Vídeo":
            file_path, _ = QFileDialog.getOpenFileName(self, "Escolher Vídeo", "", "Vídeos (*.mp4 *.avi *.mov)")
        else:
            QMessageBox.information(self, "Informação", "Para Webcam, clique em 'Detectar'.")
            return

        if file_path:
            self.input_path = file_path
            self.show_input(file_path)
            self.detect_button.setEnabled(True)

    def show_input(self, file_path):
        # Exibe a imagem ou primeiro frame do vídeo
        if self.input_selector.currentText() == "Imagem":
            pixmap = QPixmap(file_path)
            self.display_label.setPixmap(pixmap.scaled(640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif self.input_selector.currentText() == "Vídeo":
            cap = cv2.VideoCapture(file_path)
            ret, frame = cap.read()
            if ret:
                self.show_frame(frame)
            cap.release()

    def detect(self):
        input_type = self.input_selector.currentText()

        if input_type == "Imagem":
            self.detect_image()
        elif input_type == "Vídeo":
            self.detect_video()
        elif input_type == "Webcam":
            self.detect_webcam()

    def detect_image(self):
        if not self.input_path:
            QMessageBox.warning(self, "Erro", "Nenhuma imagem foi selecionada!")
            return

        # Certifique-se de que o modelo YOLO existe
        if not os.path.exists(MODEL_PATH):
            QMessageBox.critical(self, "Erro", f"Modelo YOLO não encontrado em {MODEL_PATH}")
            return

        try:
            # Carregar o modelo YOLO
            model = YOLO(MODEL_PATH)
            results = model.predict(source=self.input_path, conf=0.15)
            annotated_frame = results[0].plot()

            # Mostrar a imagem processada
            self.show_frame(annotated_frame)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao processar a imagem: {str(e)}")

    def detect_video(self):
        if not self.input_path:
            QMessageBox.warning(self, "Erro", "Nenhum vídeo foi selecionado!")
            return

        # Inicia a leitura do vídeo
        self.cap = cv2.VideoCapture(self.input_path)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def detect_webcam(self):
        # Inicia a captura da webcam
        self.cap = cv2.VideoCapture(0)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if not ret:
                self.timer.stop()
                self.cap.release()
                return

            # Processar o frame com YOLO
            model = YOLO(MODEL_PATH)
            results = model.predict(source=frame, conf=0.15)
            annotated_frame = results[0].plot()

            # Mostrar o frame processado
            self.show_frame(annotated_frame)

    def show_frame(self, frame):
        # Converte o frame para exibição no QLabel
        height, width, channels = frame.shape
        bytes_per_line = channels * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(q_image)
        self.display_label.setPixmap(pixmap.scaled(640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def close_application(self):
        # Fecha o aplicativo
        if self.cap:
            self.cap.release()
        self.timer.stop()
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
