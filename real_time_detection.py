import cv2
import torch
import paho.mqtt.client as mqtt
import time

# Configuration de la connexion MQTT
broker = "mqtt.eclipse.org"  # Remplacez par votre broker MQTT
port = 1883
topic = "iot/detection"

# Initialiser le client MQTT
client = mqtt.Client()
client.connect(broker, port)

# Charger le modèle YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Modèle pré-entraîné

# Ouvrir la caméra
cap = cv2.VideoCapture(0)  # 0 pour la webcam par défaut
if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la caméra")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur : impossible de lire une image")
        break

    # Détection des objets
    results = model(frame)

    # Afficher les résultats
    results.render()  # Modifie le cadre pour afficher les détections

    # Publier les résultats sur MQTT
    detections = results.xyxy[0].tolist()  # Détails des détections
    for *box, conf, cls in detections:
        msg = f"Détection : Classe {int(cls)} avec confiance {conf:.2f}"
        client.publish(topic, msg)
        print(msg)

    # Afficher l'image
    cv2.imshow('Détection en Temps Réel', frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
