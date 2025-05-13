import torch
import cv2
# Load the custom YOLOv5 model trained for helmet detection
model = torch.hub.load('ultralytics/yolov5', 'custom', path='helmet_detection.pt', force_reload=True)
# Open webcam or video file
cap = cv2.VideoCapture(0)  # Use 0 for webcam or 'video.mp4' for file
while cap.isOpened():
ret, frame = cap.read()
if not ret:
 break
 # Run detection
 results = model(frame)
 # Convert results to renderable image
 rendered_frame = results.render()[0]
 # Show the output
cv2.imshow('Helmet Detection - Construction Safety', rendered_frame)
# Exit on ESC key
if cv2.waitKey(1) & 0xFF == 27:
break
cap.release()
cv2.destroyAllWindows()
