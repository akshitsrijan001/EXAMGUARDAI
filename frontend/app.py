from flask import Flask, render_template, Response, send_file
import subprocess
import os
import json
import sys
import cv2
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Base directory of frontend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("BASE_DIR =", BASE_DIR)
print("TEMPLATES EXISTS =", os.path.exists(os.path.join(BASE_DIR, "templates")))
print("LOGIN EXISTS =", os.path.exists(os.path.join(BASE_DIR, "templates", "login.html")))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/verify")
def verify():

    result = subprocess.run(
        [sys.executable, "backend/verify_candidate.py"],
        capture_output=True,
        text=True
    )

    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)

    if "VERIFIED" in result.stdout:
        return {"status": "success"}

    return {"status": "failed"}


@app.route("/instructions")
def instructions():
    return render_template("instructions.html")


@app.route("/exam")
def exam():
    return render_template("exam.html")


@app.route("/result")
def result():

    monitor_file = os.path.join(
        os.path.dirname(BASE_DIR),
        "backend",
        "monitor_data.json"
    )

    try:
        with open(monitor_file, "r") as f:
            data = json.load(f)

        faces = data.get("faces", 0)
        violations = data.get("violations", 0)

    except Exception as e:
        print("Error reading monitor_data.json:", e)

        faces = 0
        violations = 0

    evidence_folder = os.path.join(
        os.path.dirname(BASE_DIR),
        "backend",
        "evidence"
    )

    evidence_count = 0

    if os.path.exists(evidence_folder):

        for root, dirs, files in os.walk(evidence_folder):

            evidence_count += len([
                file
                for file in files
                if file.endswith(".jpg")
            ])

    print("RESULT PAGE")
    print("Monitor file:", monitor_file)
    print("Faces:", faces)
    print("Violations:", violations)
    print("Evidence:", evidence_count)

    return render_template(
        "result.html",
        faces=faces,
        violations=violations,
        evidence_count=evidence_count
    )


@app.route("/monitor")
def monitor():

    monitor_file = os.path.join(
        os.path.dirname(BASE_DIR),
        "backend",
        "monitor_data.json"
    )

    try:

        with open(monitor_file, "r") as f:
            data = json.load(f)

        return data

    except Exception as e:

        print(f"Error reading monitor_data.json: {e}")

        return {
            "faces": 0,
            "violations": 0,
            "error": str(e)
        }


@app.route("/video_feed")
def video_feed():

    def generate():

        cap = cv2.VideoCapture(0)

        while True:

            success, frame = cap.read()

            if not success:
                break

            _, buffer = cv2.imencode(".jpg", frame)

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n"
                + buffer.tobytes()
                + b"\r\n"
            )

        cap.release()

    return Response(
        generate(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )
@app.route("/download_report")
def download_report():

    monitor_file = os.path.join(
         os.path.dirname(BASE_DIR),
        "backend",
        "monitor_data.json"
    )

    try:
        with open(monitor_file, "r") as f:
            data = json.load(f)

        faces = data.get("faces", 0)
        violations = data.get("violations", 0)

    except:
        faces = 0
        violations = 0

    evidence_folder = os.path.join(
        os.path.dirname(BASE_DIR),
        "backend",
        "evidence"
    )

    evidence_count = 0

    if os.path.exists(evidence_folder):

        for root, dirs, files in os.walk(evidence_folder):
            evidence_count += len(
                [f for f in files if f.endswith(".jpg")]
            )

    pdf_file = os.path.join(BASE_DIR, "exam_report.pdf")

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = [

        Paragraph("ExamGuard AI Monitoring Report",
                  styles["Title"]),

        Spacer(1, 20),

        Paragraph("Candidate: Srijan Akshit",
                  styles["Normal"]),

        Paragraph(f"Final Face Count: {faces}",
                  styles["Normal"]),

        Paragraph(f"Total Violations: {violations}",
                  styles["Normal"]),

        Paragraph(f"Evidence Captured: {evidence_count}",
                  styles["Normal"]),

        Spacer(1, 20),

        Paragraph("Report Generated Successfully",
                  styles["Heading2"])

    ]
    print("PDF Faces =", faces)
    print("PDF Violations =", violations)
    print("PDF Evidence =", evidence_count)
    doc.build(content)

    return send_file(
        pdf_file,
        as_attachment=True
    )

if __name__ == "__main__":

    print("Templates Path:", os.path.join(BASE_DIR, "templates"))
    print("Static Path:", os.path.join(BASE_DIR, "static"))

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )