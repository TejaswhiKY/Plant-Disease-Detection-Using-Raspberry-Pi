from picamera2 import Picamera2
import time
import os

def capture_image():
    os.makedirs("uploads", exist_ok=True)

    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)

    picam2.start()
    time.sleep(2)

    image_path = "uploads/capture.jpg"
    picam2.capture_file(image_path)

    picam2.stop()
    picam2.close()

    return image_path
