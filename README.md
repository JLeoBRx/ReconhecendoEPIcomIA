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
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
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
Uso:
Escolha a entrada:
Selecione "Imagem", "Vídeo" ou "Webcam" no menu dropdown.
Carregue o arquivo (se necessário):
Clique em "Escolher Arquivo" para carregar uma imagem ou vídeo.
Clique em Detectar:
O software processará a entrada e exibirá os resultados.
Sair:
Use o botão "Sair" para fechar o aplicativo.
Estrutura do Projeto:
main.py: Código principal do aplicativo, incluindo a interface gráfica e a lógica de detecção.
requirements.txt: Lista de dependências necessárias para executar o projeto.
best.pt: Modelo YOLO utilizado para detecção (não incluído no repositório; deve ser baixado separadamente).
Design e Decisões:
A interface foi construída com foco em simplicidade e acessibilidade.
Utilizamos o modelo YOLO pela sua eficiência e precisão na detecção de objetos.
Escolhemos PyQt5 por sua capacidade de criar GUIs robustas e personalizáveis.
Requisitos do Sistema:
Python: Versão 3.11.4.
Node.js: Versão 18.20.4.
Sistema operacional com suporte para Python e Node.js (Windows, Linux, ou Mac).
Possíveis Melhorias Futuras:
Implementação de um sistema de relatório para exportar os resultados das detecções.
Adicionar suporte a múltiplos idiomas na interface.
Melhorar a performance para dispositivos de baixo custo.




Explicação do Código
O projeto "Reconhecendo EPI com IA" utiliza Python para criar uma interface gráfica baseada em PyQt5 que permite o reconhecimento de Equipamentos de Proteção Individual (EPI) em imagens, vídeos e streams de webcam. Ele combina a funcionalidade do modelo YOLO (You Only Look Once) para detecção de objetos com uma interface gráfica amigável para o usuário.

Principais Componentes do Código
Bibliotecas Utilizadas
PyQt5: Para a construção da interface gráfica, incluindo botões, layouts, e exibição de resultados.
OpenCV: Para manipulação de imagens e vídeos.
Ultralytics YOLO: Para a detecção de objetos nos frames (imagens e vídeos).
Python Core Libraries: Como os e sys para controle de arquivos e configurações.
Estrutura do Código
Classe MainWindow

Configura a janela principal da aplicação.
Define o título, tamanho da janela e integra o widget principal (MainWidget).
Classe MainWidget

Contém toda a lógica da interface gráfica e funcionalidade principal.
Inclui:
Título: Exibe o nome da aplicação.
Seletor de Entrada: Um QComboBox para escolher entre Imagem, Vídeo ou Webcam.
Botões:
"Escolher Arquivo": Permite selecionar imagens ou vídeos do sistema.
"Detectar": Inicia o processo de detecção.
"Sair": Fecha o aplicativo.
Display de Resultado: Uma área onde a imagem ou vídeo processado é exibido.
Usa layouts do PyQt5 (QVBoxLayout e QHBoxLayout) para organizar os elementos.
Método choose_file

Permite que o usuário selecione um arquivo de imagem ou vídeo.
Exibe a entrada selecionada no display antes do processamento.
Método detect

Executa a detecção de acordo com o tipo de entrada:
Imagem: Processa uma imagem estática.
Vídeo: Processa cada frame do vídeo.
Webcam: Captura frames ao vivo da câmera do computador.
Método detect_image

Carrega e processa uma imagem com o modelo YOLO.
Exibe a imagem com as detecções (ex.: caixas delimitadoras em torno dos EPIs detectados).
Método detect_video

Processa um vídeo carregado pelo usuário.
Analisa frame por frame e exibe as detecções em tempo real.
Método detect_webcam

Conecta-se à webcam do computador.
Processa e exibe frames em tempo real com as detecções feitas pelo YOLO.
Método show_frame

Converte frames processados pelo OpenCV para o formato compatível com o PyQt5 (QImage) e os exibe no widget.
Modelo YOLO

O caminho do modelo YOLO é definido como uma constante (MODEL_PATH).
O modelo é carregado para processar entradas de imagem, vídeo e webcam.
Os resultados do YOLO são exibidos diretamente no display da aplicação.
Encerramento do Aplicativo

Garante que todos os recursos, como captura de vídeo e timers, sejam liberados ao fechar o programa.
Fluxo de Execução
O usuário escolhe o tipo de entrada: Imagem, Vídeo ou Webcam.
Dependendo da escolha:
Imagem: O usuário carrega uma imagem e clica em "Detectar". A imagem processada é exibida com as detecções.
Vídeo: O usuário carrega um vídeo e clica em "Detectar". Os frames processados são exibidos em tempo real.
Webcam: O usuário clica em "Detectar". A captura da webcam é exibida com as detecções.
O modelo YOLO analisa as entradas e identifica os EPIs.
O resultado é exibido na interface.
O usuário pode encerrar o programa clicando em "Sair".
Principais Decisões de Design
Interface Intuitiva: Um layout simples para que qualquer pessoa consiga usar.
Modularidade: O código é dividido em métodos claros e reutilizáveis.
Robustez: Verificações para garantir que os arquivos ou dispositivos necessários (como o modelo YOLO) estão disponíveis antes de executar.