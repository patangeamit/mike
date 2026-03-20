import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN, OLLAMA_URL, MODEL

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user = update.message.from_user

    username = user.username or user.first_name or "mysterious human"
    if not user_text:
        return

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": user_text,
                "stream": False
            },
            timeout=60
        )

        reply = response.json()["response"]

        reply = reply[:4000]
        print(f"@{username}")
        print(f"User: {user_text}\nBot: {reply}\n---")
        await update.message.reply_text(reply)

    except Exception as e:
        print( f"Error: {e}")
        await update.message.reply_text("Model decided to take a day off.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()