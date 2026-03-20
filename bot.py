import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN, OLLAMA_URL, MODEL
from pypdf import PdfReader
from collections import defaultdict
import json
memory = defaultdict(list)
MAX_HISTORY = 5  # keep it small, you're not writing a novel
def load_resume():
    reader = PdfReader("resume.pdf")
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

RESUME_TEXT = load_resume()
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user = update.message.from_user
    user_id = user.id

    username = user.username or user.first_name or "mysterious human"
    # 1. add user message FIRST
    memory[user_id].append(f"User: {user_text}")

    # 2. trim memory
    memory[user_id] = memory[user_id][-MAX_HISTORY:]

    # 3. build history string (no json nonsense)
    history = "\n".join(memory[user_id])

    # 4. build prompt
    prompt = f"""
You are a helpful assistant.

Conversation so far:
{history}

Assistant:
    """
    # print(f'Prompt: {prompt}\n')
    if not user_text:
        return
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "keep_alive": "10s"
            },
            timeout=60,
        )

        reply = response.json()["response"]

        reply = reply[:4000]
        print(f"@{username}")
        print(f"Bot: {reply}\n---")
        await update.message.reply_text(reply)
        print(f"Memory for user {user_id}:")
        for item in memory[user_id]:
            print(item)
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