import time
import cv2
from deepface import DeepFace

# Variables
last_check = 0
current_name = "Unknown"
current_color = (0, 0, 255)  # Red by default

# Webcam
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # Run recognition every 8 seconds
    if time.time() - last_check > 8:

        last_check = time.time()

        cv2.imwrite("temp.jpg", frame)

        try:

            result = DeepFace.find(
                img_path="temp.jpg",
                db_path="dataset",
                model_name="Facenet512",
                enforce_detection=True,
                silent=True
            )

            if len(result[0]) > 0:

                identity = result[0].iloc[0]["identity"]

                current_name = identity.split("\\")[-2]

                current_color = (0, 255, 0)  # Green

            else:

                current_name = "Unknown"
                current_color = (0, 0, 255)  # Red

        except:

            current_name = "Unknown"
            current_color = (0, 0, 255)  # Red

    # Display result
    cv2.putText(
        frame,
        f"Detected: {current_name}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        current_color,
        2
    )

    cv2.imshow("ExamGuard Live Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()