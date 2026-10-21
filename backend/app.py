
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Wi-Fi Faculty Attendance System Backend is running!",
        "status": "success"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Faculty Attendance System"
    })


if __name__ == "__main__":
    app.run(debug=True)
