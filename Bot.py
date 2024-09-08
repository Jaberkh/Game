from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler

# توکن بات خود را وارد کنید
TOKEN = '7494538640:AAFapduSliXBCsPXsaHc9Oxn62pdRd5oEzc'

# تابع شروع
async def start(update: Update, context):
    # ایجاد دکمه شیشه‌ای که به WebApp لینک می‌دهد
    keyboard = [
        [InlineKeyboardButton(text="شروع بازی", web_app=WebAppInfo(url="https://jaberkh.github.io/WebApp/index.html"))]
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
    main()
