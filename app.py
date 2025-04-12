from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Line Bot is Running"

@app.route("/callback", methods=['POST'])
def callback():
    print("有人打 webhook 了")
    return 'OK', 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
