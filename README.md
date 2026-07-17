# 🌿 Plant Disease Detection Using Raspberry Pi

An AI-based Plant Disease Detection System using Raspberry Pi, Python, OpenCV, Flask, and TensorFlow Lite for real-time plant disease prediction.

---

## 📌 Project Overview

This project uses a Raspberry Pi camera or uploaded leaf images to detect plant diseases using a TensorFlow Lite model. The captured image is preprocessed and passed to the AI model, which predicts the disease along with a confidence score. The result is displayed on a Flask web application and an OLED display.

---

## 🎯 Objective

To develop a low-cost, portable, and intelligent plant disease detection system that enables farmers and researchers to identify plant diseases quickly and accurately using Raspberry Pi and Artificial Intelligence.

---

## ✨ Features

- Real-time image capture using Raspberry Pi Camera
- Image upload through Flask web application
- TensorFlow Lite model for fast prediction
- Displays disease name and confidence score
- OLED display support
- Lightweight and suitable for edge AI applications

---

## 🛠 Hardware Requirements

- Raspberry Pi 4 / Raspberry Pi 5
- Raspberry Pi Camera Module
- SSD1306 OLED Display (Optional)
- Micro SD Card (32GB or above)
- Power Adapter

---

## 💻 Software Requirements

- Raspberry Pi OS
- Python 3
- Flask
- OpenCV
- TensorFlow Lite Runtime
- NumPy
- Pillow

---

## 📂 Project Structure

```
Plant-Disease-Detection-Using-Raspberry-Pi/
│
├── app.py
├── model.tflite
├── labels.txt
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── uploads/
│
└── images/
    └── output.png
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/TejaswhiKY/Plant-Disease-Detection-Using-Raspberry-Pi.git
```

Go to the project folder

```bash
cd Plant-Disease-Detection-Using-Raspberry-Pi
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Run the Flask application

```bash
python3 app.py
```

Open your browser and visit

```
http://localhost:5000
```

or

```
http://<RaspberryPi-IP>:5000
```

---

## 🧠 Working

1. Capture image using Raspberry Pi Camera or upload an image.
2. Image is resized and normalized.
3. TensorFlow Lite model processes the image.
4. Disease name and confidence score are predicted.
5. Result is displayed on Flask webpage.
6. OLED displays the prediction.

---

## 📷 Output

- Uploaded/Captured Leaf Image
- Predicted Disease Name
- Confidence Score
- OLED Display Output

---

## 📚 Technologies Used

- Python
- Raspberry Pi
- Flask
- OpenCV
- TensorFlow Lite
- HTML
- CSS

---

## 📈 Future Enhancements

- Support multiple crop diseases
- Mobile application integration
- Cloud database storage
- Disease treatment recommendations
- IoT monitoring dashboard

---

## 👩‍💻 Author

**Tejaswhi K Y**

Electronics and Communication Engineering

Bapuji Institute of Engineering and Technology

---

## 📄 License

This project is licensed under the MIT License.
