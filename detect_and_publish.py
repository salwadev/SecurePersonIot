import cv2
import paho.mqtt.client as mqtt
import torch

# Paramètres MQTT
MQTT_BROKER = "localhost"  # Adresse de votre broker MQTT
MQTT_TOPIC = "test/MQTT"  # Topic sur lequel publier

# Initialisation du client MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER)

# Chargement du modèle YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialisation de la caméra
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Détection d'objets
    results = model(frame)

    # Afficher les résultats
    results.show()

    # Publier les résultats
    detections = results.pandas().xyxy[0]  # Convertir les résultats en DataFrame
    if not detections.empty:
        message = detections.to_json(orient="records")  # Convertir en JSON
        client.publish(MQTT_TOPIC, message)  # Publier sur le topic

    # Sortie de la boucle avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libération des ressources
cap.release()
cv2.destroyAllWindows()
client.disconnect()
