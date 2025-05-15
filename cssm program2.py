import cv2
import torch

# Load YOLOv5 model (you can use 'yolov5s' or a custom trained one)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')  # Replace 'best.pt' with your model

# Load image
image_path = '0b7b6dfd-b190-4179-bf80-8648cb87f1b9.png'
img = cv2.imread(image_path)

# Inference
results = model(img)

# Extract detection results
labels, cords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
n = len(labels)
height, width = img.shape[:2]
violation = False

# Class map (customize this to your model's labels)
class_map = {0: 'helmet', 1: 'vest'}

# Draw boxes and labels
for i in range(n):
    row = cords[i]
    if row[4] >= 0.5:  # Confidence threshold
        x1, y1, x2, y2 = int(row[0]*width), int(row[1]*height), int(row[2]*width), int(row[3]*height)
        cls = int(labels[i])
        label = f"{class_map.get(cls, 'unknown')} {row[4]:.2f}"
        color = (0, 255, 0)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    else:
        violation = True

# If safety gear is missing
if violation or n < 2:  # If less than 2 gear items (helmet & vest) are detected
    cv2.putText(img, '⚠️ Safety Violation Detected!', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 4)

# Show or save output
cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
