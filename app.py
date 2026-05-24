from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Ubuntu 24 Binder Working"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
