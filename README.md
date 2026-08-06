# Real-Time Facial Emotion Recognition

Live webcam app that detects faces with OpenCV's Haar Cascade and classifies
each face's emotion (angry, disgust, fear, happy, sad, surprise, neutral)
using [DeepFace](https://github.com/serengil/deepface).

## Demo
Detected faces are boxed in green with the predicted dominant emotion
labeled above the box, updated live frame by frame.

## Requirements
- Python 3.8+
- A webcam

## Setup
```bash
git clone <this-repo-url>
cd emotion-tracker
pip install -r requirements.txt
python emotion_tracker.py
```

On first run, DeepFace will automatically download its pretrained emotion
model weights (one-time, requires internet access).

## Usage
Run the script and a window will open showing your webcam feed with live
emotion labels. Press **q** to quit.

```bash
python emotion_tracker.py
```

## How it works
1. **Face detection** — each frame is converted to grayscale and passed to
   OpenCV's `haarcascade_frontalface_default.xml` classifier to locate faces.
2. **Emotion classification** — each detected face region is cropped and
   passed to DeepFace, which predicts the dominant emotion.
3. **Annotation** — a bounding box and emotion label are drawn on the frame
   in real time.

## Project structure
```
emotion-tracker/
├── emotion_tracker.py               # main application
├── haarcascade_frontalface_default.xml  # OpenCV face detector
├── requirements.txt
└── README.md
```

## Notes
- If the webcam doesn't open, make sure no other application (Zoom, Teams,
  etc.) is using it, and that camera permissions are granted.
- DeepFace's first call per session is slower as it loads the model into
  memory; subsequent frames run faster.
