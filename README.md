   ExamGuard AI

AI-powered online examination proctoring system that monitors candidates in real time and detects suspicious activities during online assessments.

---

## Features

### Candidate Verification
- Face capture and verification before exam start
- Prevents unauthorized candidates from taking exams

### Live AI Monitoring
- Real-time webcam monitoring
- Continuous face detection using OpenCV

### Violation Detection
- No Face Detection
- Multiple Face Detection
- Tab Switching Detection

### Evidence Collection
- Automatically captures screenshots when violations occur
- Stores evidence for administrator review

### Risk Analysis Dashboard
- Interactive Admin Dashboard
- Violation Analytics Chart
- Risk Distribution Visualization
- Candidate Search Functionality

### Reporting System
- Automated PDF Report Generation
- Candidate Activity Summary
- Violation Statistics

---

## Technology Stack

### Frontend
- HTML
- CSS
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

---

## Project Structure

```
ExamGuardAI/
│
├── frontend/
│   ├── templates/
│   ├── static/
│   └── app.py
│
├── backend/
│   ├── face_detection.py
│   ├── exam_monitor.py
│   ├── verify_candidate.py
│   └── evidence/
│
├── database/
│
├── requirements.txt
└── README.md
```

---

## Workflow

1. Candidate Login
2. Identity Verification
3. Exam Instructions
4. Live Exam Monitoring
5. AI Violation Detection
6. Evidence Capture
7. Report Generation
8. Admin Dashboard Review

---

## Detected Violations

| Violation | Description |
|------------|------------|
| No Face | Candidate leaves camera view |
| Multiple Faces | Additional person detected |
| Tab Switch | Candidate leaves exam window |

---

## Future Improvements

- Deep Learning Based Face Recognition
- Head Pose Estimation
- Mobile Device Detection
- Cloud Deployment
- Multi-Candidate Analytics

---

## Author

**Srijan Akshit**

AI & Computer Vision Project


## Privacy Notice

The facial dataset used during development and testing is intentionally excluded from this public repository for privacy reasons.

To test the application, users must create their own local dataset containing authorized candidate images.

No personal training images used during development are included in this repository.
