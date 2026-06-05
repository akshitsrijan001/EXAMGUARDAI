import cv2
import json
import os
import time
import monitor_state

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Path to monitor_data.json
MONITOR_FILE = os.path.join(
    os.path.dirname(__file__),
    "monitor_data.json"
)

# Create evidence folder if it doesn't exist
os.makedirs("evidence", exist_ok=True)

# Open Webcam
cap = cv2.VideoCapture(0)

last_capture_time = 0
last_state = "normal"

while True:

    success, frame = cap.read()

    if not success:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(100, 100)
    )

    face_count = len(faces)

    # Update monitor state
    monitor_state.face_count = face_count

    # -----------------------
    # FACE STATUS
    # -----------------------

    if face_count == 1:

        last_state = "normal"

        status_text = "Face Detected"

        color = (0, 255, 0)

    elif face_count > 1:

        if last_state != "multiple":

            monitor_state.violation_count += 1

            last_state = "multiple"

            current_time = time.time()

            if current_time - last_capture_time > 5:

                filename = (
                    f"evidence/multiple_faces_"
                    f"{int(current_time)}.jpg"
                )

                cv2.imwrite(
                    filename,
                    frame
                )

                last_capture_time = current_time

        status_text = "MULTIPLE FACES DETECTED"

        color = (0, 0, 255)

    else:

        if last_state != "noface":

            monitor_state.violation_count += 1

            last_state = "noface"

            current_time = time.time()

            if current_time - last_capture_time > 5:

                filename = (
                    f"evidence/no_face_"
                    f"{int(current_time)}.jpg"
                )

                cv2.imwrite(
                    filename,
                    frame
                )

                last_capture_time = current_time

        status_text = "NO FACE DETECTED"

        color = (0, 0, 255)

    # -----------------------
    # SAVE DATA FOR FLASK
    # -----------------------

    data = {
        "faces": face_count,
        "violations": monitor_state.violation_count
    }

    with open(
        MONITOR_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f
        )

    # -----------------------
    # DISPLAY STATUS
    # -----------------------

    cv2.putText(
        frame,
        status_text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    # Draw face rectangles
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            color,
            2
        )

    # Show webcam
    cv2.imshow(
        "ExamGuard Face Detection",
        frame
    )

    # Exit with ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()