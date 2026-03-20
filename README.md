# ✋ Hand Gesture Recognition System

A real-time **Hand Gesture Recognition** project built using **Python, OpenCV, and MediaPipe**.
This system detects hand landmarks from a webcam feed and interprets gestures such as finger counting and sign language inputs.

---

## 📌 Project Overview

This project uses computer vision techniques to track hand movements and recognize gestures in real-time. It leverages MediaPipe’s hand tracking model to extract 21 key landmarks from the hand and applies logic or machine learning to interpret gestures.

---

## 🚀 Features

* ✅ Real-time hand tracking using webcam
* ✅ Detection of 21 hand landmarks
* ✅ Finger counting (0–5)
* ✅ Custom gesture recognition
* ✅ Dataset creation for training
* ✅ Machine learning-based gesture classification
* ✅ Modular and extensible code structure

---

## 🛠️ Tech Stack

* **Python 3.11**
* **OpenCV** – for video capture and image processing
* **MediaPipe** – for hand landmark detection
* **NumPy** – for numerical computations
* **Scikit-learn** *(optional)* – for training ML models

---

## 📂 Project Structure

```
Hand_Gesture_project/
│
├── first.py               # Basic MediaPipe hand detection
├── fingerCount.py         # Finger counting logic
├── sign_lang.py           # Gesture recognition (sign language)
├── dataset.py             # Dataset collection script
├── train_model.py         # Train ML model on dataset
├── test_ai.py             # Test trained model
│
├── Data/
│   └── sign_dataset.csv   # Collected gesture data
│
├── sign_model.pkl         # Trained ML model
│
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
└── .gitignore             # Ignored files
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository


git clone https://github.com/your-username/Hand-Gesture--Recognition.git
cd Hand-Gesture--Recognition


### 2️⃣ Create virtual environment


python -m venv venv
venv\Scripts\activate   # Windows


### 3️⃣ Install dependencies


pip install -r requirements.txt

Or manually:

pip install mediapipe==0.10.9 opencv-python numpy scikit-learn

---

## ▶️ How to Run

### 🔹 Basic Hand Tracking

python first.py


### 🔹 Finger Counting

python fingerCount.py


### 🔹 Collect Dataset

python dataset.py


### 🔹 Train Model

python train_model.py


### 🔹 Test AI Model


python test_ai.py


---

## 🧠 How It Works

### 1. Video Capture

* OpenCV captures real-time frames from the webcam.

### 2. Hand Detection

* MediaPipe detects hands and extracts **21 landmarks**.

### 3. Landmark Processing

* Each landmark provides `(x, y, z)` coordinates.
* These coordinates are used to analyze finger positions.

### 4. Gesture Recognition

* Rule-based logic → for finger counting
* ML-based model → for complex gestures

---

## ✋ Hand Landmarks

MediaPipe detects 21 key points on the hand:

* Fingertips
* Finger joints
* Wrist

These are used to determine gestures by comparing positions.

---

## 📊 Dataset & Model

* Dataset is stored in CSV format (`sign_dataset.csv`)
* Each row contains landmark coordinates
* Labels represent gestures (YES / NO / custom signs)
* Model is trained using Scikit-learn and saved as `.pkl`

---

## 📌 Applications

* Human-computer interaction
* Touchless interfaces
* Virtual control systems
* Accessibility tools
* Gaming and AR/VR

---

## 🚧 Future Improvements

* 🔹 Gesture-based volume control
* 🔹 Virtual mouse using hand tracking
* 🔹 Full sign language recognition
* 🔹 Deep learning (CNN/LSTM models)
* 🔹 GUI dashboard

---

## ⚠️ Known Issues

* Works best with **Python 3.10/3.11**
* Webcam must be accessible (Windows recommended over WSL)

---

## 👨‍💻 Author

**Aditya (Addy)**
GitHub: https://github.com/rajaditya-dev

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
