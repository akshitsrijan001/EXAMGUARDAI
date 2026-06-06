import sys

print("Python:", sys.executable)

from deepface import DeepFace
import cv2
import os

print("Starting Verification...")

# Open webcam
cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:
    cv2.imwrite("temp.jpg", frame)

cap.release()

dataset_path = "dataset/Srijan"

verified = False

for image in os.listdir(dataset_path):

    image_path = os.path.join(dataset_path, image)

    try:

        result = DeepFace.verify(
            img1_path="temp.jpg",
            img2_path=image_path,
            enforce_detection=False
        )

        if result["verified"]:
            verified = True
            break

    except:
        pass

if verified:
    print("VERIFIED")
else:
    print("NOT VERIFIED")