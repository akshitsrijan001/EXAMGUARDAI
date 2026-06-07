# ExamGuard AI

AI-powered online examination proctoring system designed to monitor candidates during online assessments and detect suspicious behavior in real time.

---

## Features

### Candidate Verification

* Face recognition based candidate authentication before exam start.
* Ensures only registered candidates can access the examination.

### AI Face Monitoring

* Continuous webcam monitoring during the exam.
* Detects face presence throughout the assessment.

### Multiple Face Detection

* Detects the presence of more than one face in the camera frame.
* Records violations for suspicious activity.

### No Face Detection

* Detects when the candidate leaves the camera frame.
* Logs violations after a configurable duration.

### Evidence Collection

* Automatically captures screenshots during violations.
* Stores evidence for later review.

### Violation Tracking

* Maintains a running count of suspicious events.
* Displays live violation statistics.
* Tab switching detection during examination.

### Real-Time Monitoring Dashboard

* Displays:

  * Faces detected
  * Violation count
  * Monitoring status

### Online Examination Module

* Multiple-choice question interface.
* Question navigation palette.
* Previous / Next controls.
* Mark for Review functionality.
* Countdown timer.

### Monitoring Report

* Generates final examination report.
* Displays:

  * Final face count
  * Total violations
  * Evidence captured

---

## Technology Stack

### Backend

* Python
* Flask
* OpenCV
* Haar Cascade Face Detection

### Frontend

* HTML
* CSS
* JavaScript

### Version Control

* Git
* GitHub

---

## Project Structure

```text
ExamGuardAI/
│
├── backend/
│   ├── face_detection.py
│   ├── face_recognition.py
│   ├── verify_candidate.py
│   ├── monitor_state.py
│   ├── monitor_data.json
│   ├── violation_log.txt
│   └── evidence/
│
├── frontend/
│   ├── app.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── instructions.html
│   │   ├── exam.html
│   │   └── result.html
│   │
│   └── static/
│       ├── css/
│       └── js/
│
├── dataset/
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/akshitsrijan01/EXAMGUARDAI.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Application

```bash
python frontend/app.py
```

### 4. Open Browser

```text
http://127.0.0.1:5000
```

---

## Current Status

✅ Candidate Verification Implemented

✅ Real-Time Face Monitoring Implemented

✅ Multiple Face Detection Implemented

✅ No Face Detection Implemented

✅ Evidence Capture Implemented

✅ Violation Tracking Implemented

✅ Tab Switching Detection Implemented

✅ Live Monitoring Dashboard Implemented

✅ Online Examination Interface Implemented

✅ Monitoring Report Generation Implemented

---

## Future Improvements

* PDF report generation
* Database integration
* Advanced face recognition models
* Eye gaze tracking
* Tab-switch monitoring enhancements
* Deployment on cloud platforms

---

## Disclaimer

This project is developed for educational and demonstration purposes. It is not intended for production deployment without additional security, scalability, and privacy enhancements.

---

## Author

**Srijan Akshit**

ExamGuard AI – Intelligent Online Examination Proctoring System

---

## License

This project is developed for educational and research purposes.

---

## Privacy Notice

The facial dataset used for local testing and model training is intentionally excluded from this public repository for privacy reasons.

The application can be tested by creating a local dataset containing authorized user images. All personal training images used during development remain stored only on the developer's local machine and are not included in this repository.
