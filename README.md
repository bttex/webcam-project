# 🖐️ Gesture Control System

Sistema de **controle do computador por gestos de mão em tempo real**
utilizando **visão computacional**. A aplicação usa a webcam para
detectar landmarks da mão e interpretar gestos que executam **ações no
sistema operacional**, como abrir programas ou controlar volume.

------------------------------------------------------------------------

# ✨ Funcionalidades

-   Detecção de mão em tempo real via webcam
-   Reconhecimento de **gestos de dedos**
-   **Estabilização de gestos** para evitar falsos positivos
-   Execução de **comandos do sistema**
-   Arquitetura **modular e extensível**

Exemplos de automações atuais:

  Gesto               Ação
  ------------------- --------------------------
  FIST                Encerrar o programa
  OPEN_HAND           Aumentar volume
  PEACE               Diminuir volume
  GUN                 Abrir Steam
  PINCH               Mostrar área de trabalho

*(Os gestos podem ser facilmente alterados ou expandidos.)*

------------------------------------------------------------------------

# 🧠 Arquitetura do Projeto

O projeto segue um pipeline modular de processamento:

Camera\
↓\
Hand Detector\
↓\
Gesture Detector\
↓\
Gesture Classifier\
↓\
Gesture Stabilizer\
↓\
Gesture Controller\
↓\
System Actions

### Descrição das camadas

**Camera** - Inicializa e gerencia a captura da webcam.

**Hand Detector** - Usa MediaPipe para detectar landmarks da mão.

**Gesture Detector** - Analisa os landmarks para determinar o estado dos
dedos.

**Gesture Classifier** - Classifica os estados dos dedos em gestos
semânticos.

**Gesture Stabilizer** - Confirma o gesto apenas após aparecer em
múltiplos frames consecutivos.

**Gesture Controller** - Executa ações no sistema operacional.

------------------------------------------------------------------------

# 📂 Estrutura do Projeto

    gesture-control/
    │
    ├── main.py
    │
    ├── camera.py
    ├── hand_detector.py
    ├── gesture_detector.py
    │
    ├── gesture_classifier.py
    ├── gesture_stabilizer.py
    ├── gesture_controller.py
    │
    ├── hand_landmarker.task
    │
    └── README.md

------------------------------------------------------------------------

# ⚙️ Requisitos

-   **Python 3.12.3**
-   Webcam

Bibliotecas utilizadas:

-   opencv-python
-   mediapipe
-   pyautogui

------------------------------------------------------------------------

# 📦 Instalação

Clone o repositório:

    git clone https://github.com/seu-usuario/gesture-control.git
    cd gesture-control

Crie um ambiente virtual:

    python -m venv venv

Ative o ambiente virtual:

Windows:

    venv\Scripts\activate

Linux / macOS:

    source venv/bin/activate

Instale as dependências:

    pip install opencv-python mediapipe pyautogui

------------------------------------------------------------------------

# ▶️ Executando o projeto

    python main.py

Uma janela da câmera será aberta exibindo o gesto detectado.

Pressione **ESC** ou faça o gesto **FIST** para encerrar o programa.

------------------------------------------------------------------------

# 🖐️ Gestos Reconhecidos

O classificador atual identifica os seguintes padrões de dedos:

    [0,0,0,0,0]  → FIST
    [1,0,0,0,0]  → THUMBS_UP
    [1,1,0,0,0]  → GUN
    [0,1,1,0,0]  → PEACE
    [0,1,0,0,1]  → ROCK
    [1,1,1,1,1]  → OPEN_HAND
    PINCH        → Polegar + indicador próximos

------------------------------------------------------------------------

# 🧩 Personalização

Todas as automações podem ser modificadas em:

    gesture_controller.py

Exemplo:

``` python
elif gesture == "GUN":
    open_steam()
```

Você pode executar qualquer ação:

-   abrir programas
-   rodar scripts
-   controlar mídia
-   executar atalhos do sistema
-   integrar com APIs

------------------------------------------------------------------------

# 🚀 Possíveis Melhorias Futuras

-   Configuração de gestos via arquivo JSON
-   Treinamento de novos gestos
-   Sistema de perfis de comandos
-   Integração com automação residencial
-   Interface gráfica de configuração
-   Suporte multiplataforma

------------------------------------------------------------------------

# 🧑‍💻 Tecnologias Utilizadas

-   Python
-   OpenCV
-   MediaPipe
-   PyAutoGUI

------------------------------------------------------------------------

# 📜 Licença

Projeto open-source para fins educacionais e experimentais.
