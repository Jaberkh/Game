from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# توکن بات تلگرام و URL وب‌هوک
TELEGRAM_TOKEN = '7494538640:AAFapduSliXBCsPXsaHc9Oxn62pdRd5oEzc'
WEBHOOK_URL = 'https://jaberkh.github.io/Game/index.html'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'

def set_webhook():
    """تنظیم وب‌هوک برای بات تلگرام"""
    response = requests.post(
        f'{TELEGRAM_API_URL}setWebhook',
        data={'url': WEBHOOK_URL}
    )
    print(response.json())

@app.route('/webhook', methods=['POST'])
def webhook():
    """پردازش درخواست‌های وب‌هوک"""
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    
    # پردازش پیام
    response_text = f'پیام شما: {text}'
    
    # ارسال پاسخ به تلگرام
    requests.post(TELEGRAM_API_URL + 'sendMessage', json={'chat_id': chat_id, 'text': response_text})
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # تنظیم وب‌هوک هنگام راه‌اندازی سرور
    set_webhook()
    
    # اجرای سرور Flask
    app.run(port=5000)
