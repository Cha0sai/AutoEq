from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    return 'OK', 200  # 關鍵在這邊！

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
