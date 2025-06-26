from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Welcome to Service 2 root!"})

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "service": "2"})

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Service 2"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)

