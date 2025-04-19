# YOLOv8-LiveDetect

A real-time object detection system using YOLOv8 and OpenCV. It detects objects from a webcam feed and displays bounding boxes along with confidence scores.

## Features
- ✅ Uses YOLOv8 for real-time object detection  
- ✅ Draws bounding boxes and displays class labels  
- ✅ Saves detection snapshots when 'S' is pressed  
- ✅ Press 'Q' to quit  

## Installation

Clone the repository:
```sh
git clone https://github.com/yourusername/YOLOv8-LiveDetect.git
cd YOLOv8-LiveDetect
```

Install dependencies:
```sh
pip install opencv-python torch ultralytics
```

## Requirements
- Python 3.6 or higher  
- OpenCV  
- PyTorch  
- Ultralytics YOLOv8 model

## Usage

Run the detection script:
```sh
python yolov8_live_detect.py
```

Once the webcam feed is opened:
- The program will start detecting objects in real-time using YOLOv8.
- Bounding boxes with class labels and confidence scores will appear on the objects detected.
- To save a snapshot of the current frame with detected objects, press `S`.
- To quit the program, press `Q`.

### Example Screenshots
Here are a few screenshots of the system in action:

1. **Webcam Feed with Detected Objects**  
   ![Screenshot 2025-04-19 003437](https://github.com/user-attachments/assets/c5c89771-9614-4f13-9afb-cfb22f4548ba)


2. **Saved Snapshot**  
   ![Screenshot 2025-04-19 003150](https://github.com/user-attachments/assets/61f516b9-b3d9-4965-a878-e7e8412e3e58)


## About the Technology

This project leverages the **YOLOv8** model for real-time object detection. YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system, and **YOLOv8** is one of the latest versions developed by **Ultralytics**. By utilizing **PyTorch** and **OpenCV**, the system can detect objects from a webcam feed and overlay the detection results directly on the video stream.

## Customization

You can tweak the model by training it on your custom dataset or using a different model from the **Ultralytics YOLO** repository. The `ultralytics` library makes it easy to download pre-trained models and fine-tune them.

For more information, visit the official YOLOv8 documentation here: [Ultralytics YOLOv8](https://github.com/ultralytics/yolov8).

## Notes
- The project uses **OpenCV** to handle video capture and display, and **Torch** for running the YOLOv8 model.
- To improve performance, you can use a compatible **GPU** with CUDA support.
- The detection is done in real-time, so make sure your webcam has sufficient resolution and processing capability.
