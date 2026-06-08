                                                                                                                                                                            #ExamGuard AI

**ExamGuard AI** is an AI-powered online examination proctoring system designed to monitor candidates during online assessments and detect suspicious behavior in real time. The system combines face verification, webcam monitoring, violation detection, evidence collection, reporting, and administrative oversight into a single platform.

---

## Features

### Candidate Verification

* Face recognition based candidate authentication before exam start.
* Ensures only authorized candidates can access the examination.
* Prevents impersonation attempts.

### AI-Powered Face Monitoring

* Continuous webcam monitoring throughout the examination.
* Tracks candidate presence in real time.
* Displays live monitoring statistics.

### Multiple Face Detection

* Detects the presence of more than one face in the camera frame.
* Flags suspicious behavior.
* Automatically records violations.

### No Face Detection

* Detects when the candidate leaves the camera frame.
* Logs violations after a configurable duration.
* Generates evidence for review.

### Tab Switching Detection

* Detects when the candidate switches away from the examination window.
* Records violations in real time.
* Supports browser focus monitoring.

### Evidence Collection

* Automatically captures screenshots during violations.
* Stores evidence for later review by administrators.
* Maintains a structured evidence repository.

### Violation Tracking

* Maintains a running count of detected violations.
* Records violation history throughout the examination.
* Generates violation statistics for reporting.

### Live Monitoring Dashboard

Displays real-time candidate monitoring data:

* Face Count
* Violation Count
* Monitoring Status
* Candidate Information

### Online Examination Module

* Multiple Choice Question (MCQ) interface
* Question navigation palette
* Previous / Next controls
* Mark for Review functionality
* Countdown timer
* Submit examination feature

### Monitoring Report Generation

Generates a final examination summary containing:

* Final Face Count
* Total Violations
* Evidence Captured
* Candidate Information

### PDF Report Generation

* Generates downloadable PDF reports.
* Includes monitoring statistics.
* Includes violation summary.
* Provides evidence count and candidate details.

### Administrative Dashboard

* Displays all submitted examination reports.
* Shows candidate statistics.
* Displays violations and evidence counts.
* Stores historical examination records using SQLite.

---

## Technology Stack

### Backend

* Python
* Flask
* OpenCV
* Haar Cascade Face Detection
* DeepFace
* SQLite
* ReportLab

### Frontend

* HTML5
* CSS3
* JavaScript

### Version Control

* Git
* GitHub

---

## System Architecture

1. Candidate Verification
2. Examination Login
3. Real-Time Monitoring
4. Violation Detection
5. Evidence Collection
6. Examination Submission
7. Report Generation
8. Administrative Review

---

## Project Structure

```text
ExamGuardAI/
│
├── backend/
│   ├── face_detection.py
│   ├── face_recognition.py
│   ├── verify_candidate.py
│   ├── exam_monitor.py
│   ├── monitor_state.py
│   ├── monitor_data.json
│   ├── database.py
│   ├── evidence/
│   └── violation_log.txt
│
├── frontend/
│   ├── app.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── instructions.html
│   │   ├── exam.html
│   │   ├── result.html
│   │   └── admin.html
│   │
│   └── static/
│       ├── css/
│       └── js/
│
├── dataset/
├── requirements.txt
├── README.md
└── examguard.db
```

---

## Current Status

### Core Functionality

* ✅ Candidate Verification
* ✅ Face Recognition
* ✅ Real-Time Monitoring
* ✅ Multiple Face Detection
* ✅ No Face Detection
* ✅ Tab Switching Detection
* ✅ Violation Logging
* ✅ Evidence Capture

### Examination Module

* ✅ Online Examination Interface
* ✅ Question Navigation
* ✅ Timer Functionality
* ✅ Exam Submission

### Reporting

* ✅ Monitoring Report Generation
* ✅ PDF Report Generation
* ✅ Violation Summary

### Administration

* ✅ SQLite Database Integration
* ✅ Admin Dashboard
* ✅ Historical Report Storage

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/akshitsrijan001/EXAMGUARDAI.git
cd EXAMGUARDAI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
python frontend/app.py
```

### 5. Open Browser

```text
http://127.0.0.1:5000
```

---

## Sample Workflow

1. Candidate logs in.
2. Face verification is performed.
3. Examination instructions are displayed.
4. Candidate starts examination.
5. AI monitoring runs in the background.
6. Violations are detected and recorded.
7. Evidence is captured automatically.
8. Candidate submits examination.
9. Monitoring report is generated.
10. Administrator reviews results from the dashboard.

---

## Future Enhancements

* Eye Gaze Tracking
* Head Pose Estimation
* Advanced Deep Learning Models
* Live Streaming Dashboard
* Cloud Deployment
* Multi-Candidate Monitoring
* Role-Based Admin Access
* Automated Cheating Risk Score
* Email Report Generation
* Analytics Dashboard

---

## Author

**Srijan Akshit**

ExamGuard AI – Intelligent Online Examination Proctoring System

---

## Disclaimer

This project is developed for educational, research, and demonstration purposes only.

The system is not intended for production deployment without additional enhancements related to:

* Security
* Scalability
* Data Protection
* Privacy Compliance
* Authentication Hardening

---

## Privacy Notice

The facial dataset used during development and testing is intentionally excluded from this public repository for privacy reasons.

To test the application, users must create their own local dataset containing authorized candidate images.

No personal training images used during development are included in this repository.
