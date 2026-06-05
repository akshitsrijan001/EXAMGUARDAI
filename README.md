# ExamGuard AI

AI-powered online examination proctoring system designed to monitor candidates during online assessments and detect suspicious behavior in real time.

## Features

### Candidate Verification

* Face Recognition
* Candidate Authentication
* Identity Verification before examination

### AI Proctoring

* Real-time Face Detection
* Multiple Face Detection
* No Face Detection Monitoring
* Fullscreen Enforcement
* Tab Switching Detection
* Browser Activity Monitoring

### Live Monitoring Dashboard

* Real-time Face Count
* Real-time Violation Counter
* Monitoring Status Panel
* Automated Alert System

### Evidence Collection

* Automatic Screenshot Capture
* Multiple Face Evidence Logging
* No Face Evidence Logging
* Violation Tracking
* Evidence Storage for Review

### Examination System

* Timed Online Examination
* Question Navigation Palette
* Mark for Review Functionality
* Progress Tracking
* Automatic Submission Support

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI & Computer Vision

* OpenCV
* Haar Cascade Face Detection
* DeepFace (Identity Verification)

## Project Structure

```text
frontend/
├── templates/
├── static/
├── app.py

backend/
├── face_detection.py
├── face_recognition.py
├── monitor_state.py
├── monitor_data.json
├── evidence/

dataset/

requirements.txt
README.md
```

## Current Status

### Completed

* Exam Interface
* Real-time Webcam Feed
* Face Detection Engine
* Multiple Face Detection
* No Face Detection Detection
* Evidence Screenshot Capture
* Violation Counter
* Flask Monitoring API
* GitHub Integration

### In Progress

* DeepFace Candidate Verification
* Auto Submission on Excessive Violations
* Detailed Violation Reports
* Result Analytics Dashboard

## Future Enhancements

* Eye Gaze Tracking
* Mobile Device Detection
* Audio Monitoring
* Admin Dashboard
* Cloud Evidence Storage

## Author

Srijan Akshit

## License

This project is developed for educational and research purposes.

## Privacy Notice

The facial dataset used for local testing and model training is intentionally excluded from this public repository for privacy reasons.
The application can be tested by creating a local dataset containing authorized user images. All personal training images used during development remain stored only on the developer's local machine and are not included in this repository.
