from picamera2 import Picamera2
import cv2

picam2 = Picamera2()
config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)
picam2.configure(config)
picam2.start()
from flask import Flask, render_template, request, Response
import os
import cv2
from picamera2 import Picamera2
from werkzeug.utils import secure_filename
from predict import predict_image

app = Flask(__name__)

# -----------------------------
# Upload Folder
# -----------------------------
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# -----------------------------
# Initialize Raspberry Pi Camera
# -----------------------------


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Camera Page
# -----------------------------
@app.route("/camera")
def camera():
    return render_template("camera.html")


# -----------------------------
# Live Video Feed
# -----------------------------
def generate_frames():

    while True:

        frame = picam2.capture_array()

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        ret, buffer = cv2.imencode(".jpg", frame)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )


@app.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# -----------------------------
# Capture Image from Camera
# -----------------------------
@app.route("/capture", methods=["POST"])
def capture():

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "capture.jpg"
    )

    picam2.capture_file(filepath)

    disease, confidence = predict_image(filepath)

    disease = disease.replace("_", " ")

    if confidence >= 90:
        status = "High Confidence"
    elif confidence >= 70:
        status = "Medium Confidence"
    else:
        status = "Low Confidence"

    return render_template(
        "result.html",
        disease=disease,
        confidence=round(confidence, 2),
        image_path=filepath,
        status=status
    )


# -----------------------------
# Upload Image
# -----------------------------
@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return "No file selected"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    disease, confidence = predict_image(filepath)

    disease = disease.replace("_", " ")

    if confidence >= 90:
        status = "High Confidence"
    elif confidence >= 70:
        status = "Medium Confidence"
    else:
        status = "Low Confidence"

    return render_template(
        "result.html",
        disease=disease,
        confidence=round(confidence, 2),
        image_path=filepath,
        status=status
    )


# -----------------------------
# Stop Camera Gracefully
# -----------------------------
@app.teardown_appcontext
def shutdown(exception=None):
    pass


# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
