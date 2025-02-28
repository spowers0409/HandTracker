# Finger Counting with OpenCV & MediaPipe

This project is a **real-time hand tracking and finger counting application** using **Python**, **OpenCV**, and **MediaPipe**. It detects hands via a webcam feed and counts the number of fingers extended on both hands, displaying the total in real-time.

## 📌 Features
- 🖐 **Detects up to 10 fingers** (both hands).
- 🎥 **Works in real-time** using webcam input.
- 🔄 **Mirrored video feed correction** for accurate thumb detection.
- 🎯 **Handedness detection** (Left vs. Right hand).
- 🖍 **Draws hand landmarks and connections** for better visualization.

## 🛠️ Installation
Ensure you have **Python 3.7+** installed, then install dependencies:

```bash
pip install opencv-python mediapipe numpy
```

## 🚀 Usage
Run the following command to start the finger counter:
```bash
python handtracker.py
```

## 📷 Controls:
- Press 'Q' to quit.

## 🏗️ How It Works
- Captures frames from the webcam.
- Detects hands using MediaPipe's pre-trained model.
- Identifies Left & Right hands and adjusts logic accordingly.
- Counts extended fingers by comparing landmark positions.
- Displays total fingers on the screen.
