                                                                  ExamGuard AI

## AI-Powered Online Examination Proctoring System

ExamGuard AI is an intelligent online examination proctoring system designed to monitor candidates during remote assessments and detect suspicious activities in real time. The project combines Computer Vision, Artificial Intelligence, real-time monitoring, evidence collection, analytics, and automated reporting into a unified platform.

The system helps educational institutions and organizations conduct secure online examinations by automatically monitoring candidate behavior and generating evidence whenever suspicious activity is detected.

---

## Problem Statement

Online examinations have become increasingly popular, but maintaining examination integrity remains a major challenge. Common issues include:

- Candidate impersonation
- Multiple people appearing during the exam
- Candidates leaving the examination area
- Switching tabs to search for answers
- Lack of evidence for suspicious activities

ExamGuard AI addresses these challenges through automated AI-powered monitoring and evidence collection.

---

## Project Objectives

The primary objectives of this project are:

- Verify candidate identity before examination.
- Monitor candidates continuously during online exams.
- Detect suspicious behavior automatically.
- Capture evidence whenever violations occur.
- Store examination records securely.
- Provide administrators with a centralized dashboard.
- Generate downloadable reports for review and auditing.

---

## Key Features

### Candidate Verification System

Before starting an examination, candidates must complete identity verification.

Features:

- Webcam-based face capture
- Candidate registration and verification
- Prevention of unauthorized exam access

---

### Real-Time AI Monitoring

The system continuously monitors candidates using their webcam.

Capabilities:

- Live video feed processing
- Face detection
- Candidate presence monitoring
- Real-time examination supervision

---

### No Face Detection

The system detects when the candidate leaves the camera view.

Detection Logic:

- No face visible for a specified duration
- Violation automatically recorded
- Evidence captured

Benefits:

- Prevents candidates from leaving during examinations
- Maintains examination integrity

---

### Multiple Face Detection

The system identifies when more than one person is present.

Detection Logic:

- Counts faces in each frame
- Triggers a violation if face count exceeds one

Benefits:

- Prevents collaboration during examinations
- Detects unauthorized assistance

---

### Tab Switching Detection

The system monitors whether the candidate leaves the examination tab.

Detection Logic:

- Browser visibility tracking
- Tab focus monitoring
- Automatic screenshot capture

Benefits:

- Prevents external searching during examinations
- Detects suspicious navigation behavior

---

### Evidence Collection System

Whenever a violation occurs, evidence is automatically generated.

Evidence Includes:

- Screenshots
- Captured frames
- Violation records

Purpose:

- Administrator review
- Report generation
- Audit trail creation

---

### Administrative Dashboard

The administrator dashboard provides centralized monitoring and analytics.

Features:

- Candidate report listing
- Search functionality
- Violation statistics
- Risk indicators
- Evidence viewer
- Interactive charts

Dashboard Components:

- Total Reports
- Total Violations
- AI Monitoring Status
- Violation Analytics Chart
- Risk Distribution Chart

---

### Analytics Visualization

Interactive charts provide a visual representation of examination data.

Implemented Using:

- Chart.js

Charts:

- Violation Analytics Bar Chart
- Risk Distribution Doughnut Chart

Benefits:

- Quick insights
- Improved usability
- Better decision-making

---

### PDF Report Generation

The system generates downloadable PDF reports containing:

- Candidate information
- Face count
- Violation count
- Risk assessment
- Examination summary

Library Used:

- ReportLab

---

## System Workflow

```text
Candidate Login
       │
       ▼
Identity Verification
       │
       ▼
Exam Instructions
       │
       ▼
Start Examination
       │
       ▼
Live Monitoring
       │
       ▼
Violation Detection
       │
       ├── No Face Detection
       ├── Multiple Face Detection
       └── Tab Switch Detection
       │
       ▼
Evidence Collection
       │
       ▼
Database Storage
       │
       ▼
Admin Dashboard
       │
       ▼
PDF Report Generation
```

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

### Backend

- Python
- Flask

### Computer Vision

- OpenCV

### Database

- SQLite

### Reporting

- ReportLab

### Additional Libraries

- NumPy
- JSON
- OS

---

## Project Structure

```text
ExamGuardAI/
│
├── backend/
│   ├── database.py
│   ├── face_detection.py
│   ├── face_recognition.py
│   ├── exam_monitor.py
│   ├── verify_candidate.py
│   └── evidence/
│
├── frontend/
│   ├── templates/
│   │   ├── login.html
│   │   ├── instructions.html
│   │   ├── exam.html
│   │   ├── result.html
│   │   ├── admin.html
│   │   └── evidence.html
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   └── app.py
│
├── database/
│
├── examguard.db
├── requirements.txt
└── README.md
```

---

## Detected Violations

| Violation Type | Description |
|---------------|-------------|
| No Face Detection | Candidate leaves webcam view |
| Multiple Face Detection | More than one person detected |
| Tab Switch Detection | Candidate exits examination tab |


---

## Screenshots

### Login Page
<img width="956" height="433" alt="image" src="https://github.com/user-attachments/assets/b6f65763-5d14-4ea0-9c4b-90314a73c6a7" />

### Instructions Page
<img width="529" height="431" alt="image" src="https://github.com/user-attachments/assets/ad3b8fca-90ca-46ba-b083-962885f22abf" />

### Live Examination Interface
<img width="1672" height="941" alt="image" src="https://github.com/user-attachments/assets/728a9a58-366c-42c6-bb49-3076e8edfcef" />


### Admin Dashboard
<img width="956" height="398" alt="image" src="https://github.com/user-attachments/assets/599e909f-a431-488f-b683-2b4719b0e2c2" />


### Evidence Viewer
<img width="950" height="153" alt="image" src="https://github.com/user-attachments/assets/43e9b9fd-13d6-49df-85f9-447ca6f9e6ab" />
(ACTUAL IMAGES NOT ADDED DUE TO PRIVACY CONCERNS)

---

## Future Enhancements

Potential future improvements include:

- Deep Learning based Face Recognition
- Eye Gaze Tracking
- Head Pose Estimation
- Mobile Phone Detection
- Audio Monitoring
- Cloud Deployment
- Multi-Candidate Analytics
- Real-Time Administrator Alerts
- AI-Based Cheating Probability Scoring

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Computer Vision
- Artificial Intelligence Monitoring
- Flask Web Development
- Database Management
- Data Visualization
- Automated Report Generation
- Real-Time Detection Systems
- Full-Stack Application Development

---

## Conclusion

ExamGuard AI provides a complete AI-powered online examination monitoring solution capable of verifying candidate identity, monitoring behavior in real time, detecting suspicious activities, collecting evidence, generating reports, and providing administrators with actionable insights through an interactive dashboard.

The project demonstrates the integration of Artificial Intelligence, Computer Vision, Web Development, and Data Analytics to address real-world challenges in remote examinations.

---

## Author

### Srijan Akshit

**ExamGuard AI – AI-Powered Online Examination Proctoring System**

Built using Python, Flask, OpenCV, SQLite, ReportLab, HTML, CSS, JavaScript, and Chart.js.


## Privacy Notice

The facial dataset used during development and testing is intentionally excluded from this public repository for privacy reasons.

To test the application, users must create their own local dataset containing authorized candidate images.

No personal training images used during development are included in this repository.
