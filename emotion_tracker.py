"""
Real-Time Facial Emotion Recognition
-------------------------------------
Uses OpenCV's Haar Cascade for face detection and DeepFace for
emotion classification on each detected face, live from the webcam.

Run:
    python emotion_tracker.py

Press 'q' to quit.
"""

import os
import sys

import cv2
from deepface import DeepFace

CASCADE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "haarcascade_frontalface_default.xml")

# Emotion labels DeepFace can classify (matches the FER dataset)
EMOTION_LABELS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]


def load_face_cascade(path: str) -> cv2.CascadeClassifier:
    """Load the Haar Cascade classifier and validate it actually loaded."""
    if not os.path.exists(path):
        print(f"Cascade file not found at: {path}")
        sys.exit(1)

    cascade = cv2.CascadeClassifier(path)
    if cascade.empty():
        print(f"Failed to load cascade classifier from: {path}")
        sys.exit(1)

    return cascade


def open_webcam(index: int = 0) -> cv2.VideoCapture:
    """Open the webcam and confirm it's actually available."""
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print("Could not open webcam. Check that it's connected and not in use "
              "by another application.")
        sys.exit(1)
    return cap


def main() -> None:
    face_cascade = load_face_cascade(CASCADE_PATH)
    cap = open_webcam(0)

    print("Starting real-time emotion recognition... Press 'q' to quit.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame from webcam. Stopping.")
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray_frame,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(40, 40),
            )

            for (x, y, w, h) in faces:
                face_roi = frame[y:y + h, x:x + w]

                try:
                    result = DeepFace.analyze(
                        face_roi, actions=["emotion"], enforce_detection=False
                    )
                    dominant_emotion = result[0]["dominant_emotion"]
                except Exception:
                    # Skip this face if DeepFace can't analyze the frame
                    dominant_emotion = "..."

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    dominant_emotion,
                    (x, max(0, y - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )

            cv2.imshow("DeepFER: Real-Time Emotion Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
