from deepface import DeepFace
import cv2
import os

# Open webcam
cap = cv2.VideoCapture(0)

print("Press SPACE to capture face")
print("Press ESC to exit")

while True:

    success, frame = cap.read()

    if not success:
        break

    cv2.imshow("Candidate Verification", frame)

    key = cv2.waitKey(1)

    # SPACE
    if key == 32:

        cv2.imwrite("temp.jpg", frame)

        try:

            result = DeepFace.find(
                img_path="temp.jpg",
                db_path="dataset",
                enforce_detection=False
            )

            if len(result[0]) > 0:

                identity = result[0].iloc[0]["identity"]

                print("\nMATCH FOUND")
                print(identity)

            else:

                print("\nNO MATCH FOUND")

        except Exception as e:

            print("Error:", e)

        break

    # ESC
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()