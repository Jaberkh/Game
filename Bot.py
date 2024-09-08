from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
app = Flask(__name__)

# توکن بات خود را وارد کنید
TOKEN = '7200440128:AAFE1aOYaMj0Eqozc0jp6DDDDlt-Xad9bic'

# تابع شروع
async def start(update: Update, context):
    # ایجاد دکمه شیشه‌ای که به WebApp لینک می‌دهد
    keyboard = [
        [InlineKeyboardButton(text="شروع بازی", web_app=WebAppInfo(url="https://jaberkh.github.io/Game/index.html"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ارسال پیام با دکمه WebApp
    await update.message.reply_text('روی دکمه زیر کلیک کنید تا بازی شروع شود:', reply_markup=reply_markup)

# تابع اصلی برای راه‌اندازی بات
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # هندلر برای دستور /start
    application.add_handler(CommandHandler("start", start))

    # اجرای بات به صورت polling (بدون نیاز به await)
    application.run_polling()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
