Reconhecimento de EPI com IA

Video Demo: https://youtu.be/piYG6buCN8Q

Descrição:
Este projeto é um software que utiliza Inteligência Artificial (IA) para reconhecer Equipamentos de Proteção Individual (EPI) em imagens, vídeos ou via webcam em tempo real. Ele foi desenvolvido em Python 3.11.4 com o framework PyQt5 para interface gráfica e utiliza o modelo YOLO para a detecção. Este software permite a seleção de diferentes fontes de entrada (imagem, vídeo ou webcam) e realiza a detecção de EPIs com precisão, exibindo os resultados na interface.

Funcionalidades:
Detecção de EPIs em Imagens: Carregue uma imagem no formato JPG, PNG ou JPEG e visualize os EPIs identificados diretamente na interface.
Detecção de EPIs em Vídeos: Analise vídeos em tempo real para reconhecer os EPIs em cada quadro.
Detecção via Webcam: Utilize a câmera do computador para a detecção em tempo real.
Interface Simples e Intuitiva: Desenvolvida com PyQt5, permite fácil navegação e uso por qualquer pessoa.

Tecnologias Utilizadas:
Python 3.11.4: Linguagem principal para o desenvolvimento do software.
Node.js 18.20.4: Utilizado como ambiente para bibliotecas e frameworks, se necessário.
PyQt5: Para construção da interface gráfica.
YOLO (You Only Look Once): Para a detecção e reconhecimento de objetos.
OpenCV: Para manipulação de vídeos e imagens.
Ultralytics: Biblioteca que fornece suporte ao modelo YOLO.

Instalação e Configuração:
Clone o repositório:

bash
Copiar código
git clone https://github.com/JLeoBRx/ReconhecendoEPIcomIA.git
cd ReconhecendoEPIcomIA
Crie um ambiente virtual (opcional):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
Instale as dependências: Certifique-se de que o arquivo requirements.txt está no diretório principal e execute:

bash
Copiar código
pip install -r requirements.txt
Modelo YOLO:

Baixe o modelo pré-treinado YOLO (best.pt) e coloque no caminho configurado no código: C:\yolo\best.pt.
Execute o software:

bash
Copiar código
python main.py
