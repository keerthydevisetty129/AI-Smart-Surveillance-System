# AI-Smart-Surveillance-System
# AI Smart Surveillance System using YOLOv8

## 📌 Project Overview

The **AI Smart Surveillance System** is a real-time computer vision application that uses **YOLOv8 (You Only Look Once)** and **OpenCV** to detect and monitor objects from video streams.
The system is designed to simulate intelligent surveillance by identifying objects such as **people, vehicles, mobile phones, and helmets** in real-time.

This project demonstrates how **Artificial Intelligence and Deep Learning** can be applied to build smart monitoring systems for **traffic management, workplace safety, and security surveillance**.

---

## 🎯 Objectives

* Detect objects in real-time using deep learning.
* Monitor traffic and detect vehicles automatically.
* Identify mobile phone usage in monitored areas.
* Provide a modular surveillance system that can be extended for smart city applications.

---

## 🚀 Features

* Real-time **object detection** using YOLOv8.
* **Vehicle detection** from traffic videos.
* **Mobile phone detection** for driver safety monitoring.
* **Helmet detection module** for workplace safety monitoring.
* Modular architecture with separate detection modules.
* Easy integration with new datasets and models.

---

## 🧠 Technologies Used

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy
* Deep Learning
* Computer Vision

---

## 📂 Project Structure

AI-Smart-Surveillance-System
│
├── src
│   ├── object_detection.py
│   ├── vehicle_counter.py
│   ├── phone_detection.py
│   └── helmet_detection.py
│
├── utils
│   └── tracker.py
│
├── videos
│   └── traffic.mp4
│
├── models
│   └── helmet_model.pt
│
├── run.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/AI-Smart-Surveillance-System.git

Navigate to the project folder:

cd AI-Smart-Surveillance-System

Install required libraries:

pip install -r requirements.txt

---

## ▶️ How to Run the Project

Run the main file:

python run.py

You will see a menu:

1 - Object Detection
2 - Vehicle Counting
3 - Phone Detection
4 - Helmet Detection

Enter the option number to run the corresponding module.

## 📊 Applications

This system can be used in:

* Smart traffic monitoring systems
* Road safety monitoring
* Construction site safety monitoring
* Smart city surveillance
* Driver distraction detection systems

## 👩‍💻 Author
Keerthy Devisetty

This project was developed as part of learning **Artificial Intelligence, Computer Vision, and Deep Learning applications in real-world surveillance systems**.
