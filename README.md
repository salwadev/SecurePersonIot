

## Installation

Pour installer le projet, suivez ces étapes :

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/salwadev/SecurePersonIot.git
   cd SecurePersonIot

2. Créez un environnement virtuel et activez-le :

   ```bash
    python -m venv venv
    source venv/bin/activate

3. Installez les dépendances :

   ```bash
      Install Required Packages
      pip install opencv-python torch torchvision torchaudio
      Clone YOLO Repository
      git clone <YOLO_REPOSITORY_URL>  
      Navigate to YOLO Directory
      cd Yolo
      Install YOLO Requirements
      pip install -r requirements.txt

4. Lancez l'application :

   ```bash
  
   python detect.py --source ./sunflower.jpg --weights yolov5s.pt

   Detection with MQTT
   python detect_and_publish.py  # Test with MQTT

5. MQTT Setup :

   ```bash


   Install Mosquitto
         (https://mosquitto.org/download/)
   Start Mosquitto Broker
      Open Command Prompt as Administrator:
      cd "C:\Program Files\mosquitto"
      net start mosquitto
      Test MQTT Publisher
      In the same or another Command Prompt window:
      mosquitto_pub -t "test/topic" -m "Hello MQTT"  # To test if Mosquitto is active
      Test MQTT Subscriber
      In another Command Prompt window:
      mosquitto_sub -t "test/topic"

   pour connecter broker
   mqtt.js 


