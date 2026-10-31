
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/lessons")
def lessons():
    return jsonify([
        {
            "id": 1,
            "title": "Introduction to CI/CD",
            "description": "Understand CI and CD."
        },
        {
            "id": 2,
            "title": "Git and GitHub",
            "description": "Learn version control."
        },
        {
            "id": 3,
            "title": "GitHub Actions",
            "description": "Build automated workflows."
        }
    ])


@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True)
