import os
import cv2
import numpy as np
import tensorflow as tf

# Project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Files
MODEL_PATH = os.path.join(BASE_DIR, "model", "plant_disease_model.tflite")
LABELS_PATH = os.path.join(BASE_DIR, "model", "labels.txt")

# Check model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found:\n{MODEL_PATH}")

# Check labels
if not os.path.exists(LABELS_PATH):
    raise FileNotFoundError(f"Labels file not found:\n{LABELS_PATH}")

# Load labels
with open(LABELS_PATH, "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

# Input / Output
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

height = input_details[0]["shape"][1]
width = input_details[0]["shape"][2]


def predict_image(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return "Image not found", 0

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (width, height))

    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    interpreter.set_tensor(input_details[0]["index"], img)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]["index"])[0]

    index = np.argmax(output)

    disease = labels[index]
    confidence = float(output[index]) * 100

    return disease, confidence
