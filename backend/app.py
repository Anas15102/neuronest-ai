from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

activities = [
    "Memory Game",
    "Math Puzzle",
    "Drawing Task",
    "Story Reading",
    "Shape Sorting"
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "NeuroNest Backend Running!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    age = data.get("age", 8)
    focus_score = data.get("focus_score", 5)

    if focus_score < 4:
        activity = random.choice(["Memory Game", "Shape Sorting"])
    elif 4 <= focus_score <= 6:
        activity = random.choice(["Drawing Task", "Math Puzzle"])
    else:
        activity = random.choice(["Story Reading", "Math Puzzle"])

    return jsonify({"recommendation": activity})

if __name__ == "__main__":
    app.run(debug=True)