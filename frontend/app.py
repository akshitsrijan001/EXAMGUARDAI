from flask import Flask, render_template
import os
import json

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
        return {
            "faces": 0,
            "violations": 0,
            "error": str(e)
        }


if __name__ == "__main__":

    print("Templates Path:", os.path.join(BASE_DIR, "templates"))
    print("Static Path:", os.path.join(BASE_DIR, "static"))

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )