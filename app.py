from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/entry_point.html")
def entry_point():
    return send_from_directory(".", "entry_point.html")

@app.route("/api/sentences")
def get_sentences():
    if os.path.exists("sentences.json"):
        with open("sentences.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify([]), 404

@app.route("/api/mock_tests")
def get_mock_tests():
    if os.path.exists("mock_tests.json"):
        with open("mock_tests.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify([]), 404

if __name__ == "__main__":
    print("토익스피킹 187문장 & 전 파트 실전 풀이 서버 시작: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
