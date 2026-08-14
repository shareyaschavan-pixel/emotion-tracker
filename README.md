<div align="center">

# 😊 Emotion Tracker

**Real-time facial emotion recognition** built with OpenCV and DeepFace.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Detection-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)
[![DeepFace](https://img.shields.io/badge/DeepFace-Emotion%20Analysis-FF6F00?style=flat-square)](https://github.com/serengil/deepface)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#license)

</div>

---

## ✨ Overview

Emotion Tracker uses your webcam to detect faces in real time and classify the dominant emotion being expressed — happy, sad, angry, surprised, neutral, and more — using a Haar Cascade face detector paired with DeepFace's deep-learning emotion classifier.

## 🎯 Features

- 📷 Real-time webcam face detection (Haar Cascade)
- 🧠 Deep-learning emotion classification via DeepFace
- ⚡ Lightweight — single-script, no server required
- 🖼️ Live on-screen bounding boxes and emotion labels

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Face detection | OpenCV (Haar Cascade Classifier) |
| Emotion recognition | [DeepFace](https://github.com/serengil/deepface) |
| Language | Python |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A webcam

### Installation
```bash
git clone https://github.com/shareyaschavan-pixel/emotion-tracker.git
cd emotion-tracker
pip install -r requirements.txt
```

### Run
```bash
python emotion_tracker.py
```
Press **q** to quit the live video window.

## 📂 Project Structure

```
emotion-tracker/
├── emotion_tracker.py               # Main application script
├── haarcascade_frontalface_default.xml   # Pretrained face detector
├── requirements.txt
└── README.md
```

## 🗺️ Roadmap

- [ ] Add emotion history logging/export
- [ ] Support multiple simultaneous faces with per-face labels
- [ ] Package as a standalone desktop app

## 📄 License

MIT — feel free to fork and adapt.

---

<div align="center">
Built with OpenCV + DeepFace.
</div>
