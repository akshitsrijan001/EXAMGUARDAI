from flask import Flask, render_template
import subprocess
import os
import json
import subprocess
import sys
from flask import Response
import cv2

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
    return render_template("result.html")


@app.route("/monitor")
def monitor():

    monitor_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
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

    return Response(
        generate(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )
    

if __name__ == "__main__":

    print("Templates Path:", os.path.join(BASE_DIR, "templates"))
    print("Static Path:", os.path.join(BASE_DIR, "static"))

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
    