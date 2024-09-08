from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler
from flask import Flask, request
import asyncio
import os

app = Flask(__name__)

# توکن بات خود را وارد کنید
TOKEN = '7200440128:AAFE1aOYaMj0Eqozc0jp6DDDDlt-Xad9bic'
WEBHOOK_URL = 'https://base-test.onrender.com/webhook'  # آدرس Webhook با /webhook

# تابع شروع
async def start(update: Update, context):
    # ایجاد دکمه شیشه‌ای که به WebApp لینک می‌دهد
    keyboard = [
        [InlineKeyboardButton(text="شروع بازی", web_app=WebAppInfo(url="https://jaberkh.github.io/Game/index.html"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ارسال پیام با دکمه WebApp
    await update.message.reply_text('روی دکمه زیر کلیک کنید تا بازی شروع شود:', reply_markup=reply_markup)

# تنظیم Webhook
async def set_webhook(application: Application):
    await application.bot.set_webhook(WEBHOOK_URL)

# نقطه ورود برای Webhook تلگرام
@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    update = Update.de_json(json_data, application.bot)
    application.update_queue.put(update)
    return "ok", 200

# تابع اصلی برای راه‌اندازی بات
async def main():
    global application
    application = Application.builder().token(TOKEN).build()

    # هندلر برای دستور /start
    application.add_handler(CommandHandler("start", start))

    # تنظیم Webhook در تلگرام
    await set_webhook(application)

    # اجرای اپلیکیشن
    await application.start()
    await application.updater.start_polling()

if __name__ == '__main__':
    # استفاده از پورت مشخص‌شده توسط Render
    port = int(os.environ.get("PORT", 10000))

    # اجرای اپلیکیشن Flask
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    app.run(host='0.0.0.0', port=port)
