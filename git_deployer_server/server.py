from fastapi import FastAPI, Request
from dotenv import load_dotenv

import uvicorn
import os
import telebot

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_API_KEY'))



app = FastAPI()


@app.post("/github-webhook/")
async def github_webhook():
    mk = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Перезапуск", callback_data="git_pull")
    mk.add(button)
    text = "Получено обновление с GitHub. Чтобы перезапустить, нажми на кнопку"

    try:
        bot.send_message(
            chat_id=os.getenv('ADMIN_1_ID'),
            text=text,
            reply_markup=mk
        )

        bot.send_message(
            chat_id=os.getenv('ADMIN_2_ID'),
            text=text,
            reply_markup=mk
        )
    except Exception as e:
        print(e)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
