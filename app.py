from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "LINE BOT is running."

@app.route("/callback", methods=["POST"])
def callback():
    # 接收 LINE 的資料
    body = request.get_data(as_text=True)
    print("Request body:", body)

    # 確保 LINE 測試 webhook 有回傳 200
    return 'OK', 200

if __name__ == "__main__":
    app.run()
