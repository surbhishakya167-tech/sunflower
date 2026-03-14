from flask import Flask, request, jsonify
from ai_review import analyze_submission

app = Flask(__name__)

@app.route("/review", methods=["POST"])
def review():

    data = request.json

    task = data["task"]
    submission = data["submission"]

    result = analyze_submission(task, submission)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)