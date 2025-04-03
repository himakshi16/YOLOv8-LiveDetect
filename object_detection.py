import cv2
import torch
from ultralytics import YOLO

# ✅ Load the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  

# ✅ Initialize webcam
cap = cv2.VideoCapture(0)  

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # ✅ Perform object detection
    results = model(frame)

    
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
            confidence = box.conf[0]  # Confidence score
            label = result.names[int(box.cls[0])]  # Object class label

            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # ✅ Display label & confidence score
            text = f"{label}: {confidence:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # ✅ Show the frame with detections
    cv2.imshow("Object Detector (YOLOv8)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Save an image when 'S' is pressed
        cv2.imwrite("detected_objects.jpg", frame)
        print("📸 Image saved!")

    if key == ord('q'):  # Press 'Q' to quit
        break

cap.release()
cv2.destroyAllWindows()
