from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '7494538640:AAFapduSliXBCsPXsaHc9Oxn62pdRd5oEzc'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    
    # Process the message or respond
    response_text = 'Received: ' + text
    
    # Send response back to Telegram
    requests.post(TELEGRAM_API_URL + 'sendMessage', json={'chat_id': chat_id, 'text': response_text})
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=5000)
