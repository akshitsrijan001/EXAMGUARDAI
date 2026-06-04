from tab_switch_detector import TabSwitchDetector
import cv2
import time
import winsound
from deepface import DeepFace

# -------------------------------
# Face Detector
# -------------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# -------------------------------
# Variables
# -------------------------------
last_check = 0

status_text = "Waiting For Verification..."
status_color = (255, 255, 255)

current_name = "Not Verified"

multiple_face_counter = 0
multiple_face_start_time = None
violation_screenshot_taken = False
alert_beep_played = False
no_face_start_time = None
no_face_violation_logged = False

# -------------------------------
# Webcam
# -------------------------------
tab_detector = TabSwitchDetector()
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break
    tab_detector.check_window_focus()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(80, 80)
    )

    face_count = len(faces)

    # =====================================
    # CASE 1 : NO FACE
    # =====================================
    if face_count == 0:

        multiple_face_counter = 0
        multiple_face_start_time = None
        violation_screenshot_taken = False
        alert_beep_played = False

        current_name = "No Face"
        if no_face_start_time is None:
            no_face_start_time = time.time()

        elapsed_no_face = (
            time.time() - no_face_start_time
        )

        status_text = "No Face Detected"
        status_color = (0, 255, 255)
        if elapsed_no_face >= 10:

            status_text = "ALERT: NO FACE VIOLATION"
            status_color = (0, 0, 255)

            if not no_face_violation_logged:

                winsound.Beep(1000, 500)

                timestamp = time.strftime(
                    "%Y%m%d_%H%M%S"
                )

                filename = (
                    "backend/evidence/no_face/"
                    f"no_face_{timestamp}.jpg"
                )

                cv2.imwrite(filename, frame)

                with open(
                    "backend/evidence/violation_log.txt",
                    "a"
                ) as log:

                    log.write(
                        f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                        "VIOLATION: No Face Detected\n"
                    )

                    log.write(
                        f"File: {filename}\n"
                    )

                    log.write(
                        "Severity: High\n"
                    )

                    log.write(
                        "Status: Logged\n\n"
                    )

                no_face_violation_logged = True

    # =====================================
    # CASE 2 : MULTIPLE FACES
    # =====================================
    elif face_count > 1:

        current_name = "N/A"

        multiple_face_counter += 1

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2
            )

        if multiple_face_counter >= 3:

            if multiple_face_start_time is None:
                multiple_face_start_time = time.time()

            elapsed_time = (
                time.time() - multiple_face_start_time
            )

            if elapsed_time >= 8:

                status_text = (
                    "ALERT: MULTIPLE FACE VIOLATION"
                )

                status_color = (0, 0, 255)

                if not alert_beep_played:

                    winsound.Beep(1000, 500)

                    alert_beep_played = True

                if not violation_screenshot_taken:

                    timestamp = time.strftime(
                        "%Y%m%d_%H%M%S"
                    )

                    filename = (
                        "backend/evidence/multiple_faces/"
                        f"multiple_faces_{timestamp}.jpg"
                    )

                    cv2.imwrite(
                        filename,
                        frame
                    )

                    violation_screenshot_taken = True

                    with open(
                        "backend/evidence/violation_log.txt",
                        "a"
                    ) as log:

                        log.write(
                            f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                            "VIOLATION: Multiple Faces Detected\n"
                        )

                        log.write(
                            f"File: {filename}\n"
                        )

                        log.write(
                            "Severity: High\n"
                        )

                        log.write(
                            "Status: Logged\n\n"
                        )

            else:

                remaining = max(
                    0,
                    int(8 - elapsed_time)
                )

                status_text = (
                    f"Verifying Multiple Faces... "
                    f"{remaining}s"
                )

                status_color = (
                    0,
                    255,
                    255
                )

    # =====================================
    # CASE 3 : SINGLE FACE
    # =====================================
    else:

        multiple_face_counter = 0
        multiple_face_start_time = None
        violation_screenshot_taken = False
        alert_beep_played = False
        no_face_start_time = None
        no_face_violation_logged = False

        status_text = "Exam In Progress"
        status_color = (0, 255, 0)

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        if time.time() - last_check > 10:

            last_check = time.time()

            cv2.imwrite(
                "temp.jpg",
                frame
            )

            try:

                result = DeepFace.find(
                    img_path="temp.jpg",
                    db_path="dataset",
                    model_name="Facenet512",
                    enforce_detection=False,
                    silent=True
                )

                if len(result[0]) > 0:

                    identity = (
                        result[0]
                        .iloc[0]["identity"]
                    )

                    name = identity.split("\\")[-2]

                    current_name = name

                else:

                    current_name = "Unknown"

            except:

                current_name = "Error"

                status_text = (
                    "Recognition Error"
                )

                status_color = (
                    0,
                    0,
                    255
                )

    # =====================================
    # DISPLAY STATUS
    # =====================================

    cv2.putText(
        frame,
        status_text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        status_color,
        2
    )

    cv2.putText(
        frame,
        f"Faces: {face_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Identity: {current_name}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "ExamGuard AI Monitor",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()