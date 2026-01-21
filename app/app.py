from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, WinWin Travel"


@app.route("/healthz")
def healthz():
    return jsonify({
        "env": "local",
        "service": "app",
        "status": "ok"
    })

if __name__ == "__main__":
   
    app.run(host="0.0.0.0", port=5000)
