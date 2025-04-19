# ObjectDetection/views.py

from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, redirect
import cv2
from ultralytics import YOLO

# Global toggle to start/stop the stream
is_streaming = False

def generate_frames():
    global is_streaming
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    while is_streaming and cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf[0]
                label = result.names[int(box.cls[0])]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label}: {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

def start_stream(request):
    global is_streaming
    is_streaming = True
    return redirect('home')

def stop_stream(request):
    global is_streaming
    is_streaming = False
    return redirect('home')

def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def home(request):
    global is_streaming
    return render(request, 'home.html', {'is_streaming': is_streaming})
