from ultralytics import YOLO
import cv2

# Replace "YOLOv8n-cls" with the correct model name
model = YOLO("250.pt")

results = model(source=0, save = True, show = "true")
