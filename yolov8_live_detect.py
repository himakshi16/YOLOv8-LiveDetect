import cv2
import torch
from ultralytics import YOLO


model = YOLO("yolov8n.pt")  


cap = cv2.VideoCapture(0)  

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

   
    results = model(frame)

    
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            confidence = box.conf[0] 
            label = result.names[int(box.cls[0])]  

            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            text = f"{label}: {confidence:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

  
    cv2.imshow("Object Detector (YOLOv8)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  
        cv2.imwrite("detected_objects.jpg", frame)
        print("📸 Image saved!")

    if key == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
