import cv2
import torch
import matplotlib.pyplot as plt
import numpy as np

# Load model (replace with your trained model path)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# Load image
image_path = '26d6241f-41f6-4e2c-8914-36409184772d.png'
img = cv2.imread(image_path)
height, width = img.shape[:2]

# Define Danger Zone (manual polygon)
danger_zone = np.array([[350, 500], [750, 500], [750, 650], [350, 650]])

# Draw Danger Zone
overlay = img.copy()
cv2.fillPoly(overlay, [danger_zone], (0, 0, 255))
alpha = 0.3
img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

# Detect people
results = model(img)
detections = results.pandas().xyxy[0]

# Draw detections
for _, row in detections.iterrows():
    if row['confidence'] > 0.5 and row['name'] == 'person':
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
        inside_danger = cv2.pointPolygonTest(danger_zone, (cx, cy), False) >= 0

        color = (0, 255, 0) if not inside_danger else (0, 0, 255)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        label = "Safe" if not inside_danger else "In Danger"
        cv2.putText(img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

# Show image
cv2.imshow("Construction Monitoring", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sample Sensor Data Visualization
x = np.arange(10)
y = np.random.randint(50, 100, 10)

plt.plot(x, y, label='Zone Gas Levels')
plt.axhline(75, color='r', linestyle='--', label='Threshold')
plt.title("Danger Zone Analysis")
plt.xlabel("Time")
plt.ylabel("Sensor Value")
plt.legend()
plt.show()
