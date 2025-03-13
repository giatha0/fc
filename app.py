from flask import Flask, request
import requests

app = Flask(__name__)

# Cập nhật token bot và chat_id của bạn
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Nhận được webhook:", data)
    
    # Tạo tin nhắn dựa trên payload nhận được
    message = f"Webhook nhận được: {data}"
    
    # Gửi tin nhắn tới Telegram
    send_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(send_url, json=payload)
    
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)