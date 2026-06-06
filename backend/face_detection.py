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

# Create evidence folder
os.makedirs("evidence", exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)

last_capture_time = 0
last_state = None
no_face_start = None

# Reset counters on startup
monitor_state.violation_count = 0
monitor_state.face_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(100, 100)
    )

    face_count = len(faces)

    print(
        f"Faces: {face_count}  Violations: {monitor_state.violation_count}"
    )

    # -----------------------
    # FACE STATUS
    # -----------------------

    if face_count == 1:

        status_text = "FACE DETECTED"
        color = (0, 255, 0)

        last_state = "normal"
        no_face_start = None

    elif face_count > 1:

        status_text = "MULTIPLE FACES DETECTED"
        color = (0, 0, 255)

        no_face_start = None

        if last_state != "multiple":

            monitor_state.violation_count += 1
            last_state = "multiple"

            current_time = time.time()

            if current_time - last_capture_time > 5:

                filename = (
                    f"evidence/multiple_faces_{int(current_time)}.jpg"
                )

                cv2.imwrite(
                    filename,
                    frame
                )

                last_capture_time = current_time

    else:

        status_text = "NO FACE DETECTED"
        color = (0, 0, 255)

        if no_face_start is None:
            no_face_start = time.time()

        elif time.time() - no_face_start >= 3:

            if last_state != "noface":

                monitor_state.violation_count += 1
                last_state = "noface"

                current_time = time.time()

                if current_time - last_capture_time > 5:

                    filename = (
                        f"evidence/no_face_{int(current_time)}.jpg"
                    )

                    cv2.imwrite(
                        filename,
                        frame
                    )

                    last_capture_time = current_time

    monitor_state.face_count = face_count

    # -----------------------
    # SAVE DATA FOR FLASK
    # -----------------------

    data = {
        "faces": face_count,
        "violations": monitor_state.violation_count
    }

    with open(MONITOR_FILE, "w") as f:
        json.dump(data, f)

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

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            color,
            2
        )

    cv2.imshow(
        "ExamGuard Face Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()