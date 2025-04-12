from flask import Flask, request, abort
import os
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Line Bot is Running"

@app.route("/callback", methods=['POST'])
def callback():
    # 確認是來自 LINE
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)
    
    print(f"Header: {signature}")
    print(f"Body: {body}")
    
    # 簡易回應
    return 'OK', 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
