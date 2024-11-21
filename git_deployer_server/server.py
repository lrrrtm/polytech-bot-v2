from flask import Flask, request
from dotenv import load_dotenv
import os

import telebot

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_API_KEY'))

app = Flask(__name__)


@app.route('/github-webhook/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        mk = telebot.types.InlineKeyboardMarkup(
            keyboard=[
                telebot.types.InlineKeyboardButton(text="Перезапуск", callback_data="git_pull"),
            ]
        )
        text = "Получено обновление с GitHub. Чтобы перезапустить, нажми на кнопку"

        try:
            bot.send_message(
                chat_id=os.environ['ADMIN_1_ID'],
                text=text,
                reply_markup=mk
            )

            bot.send_message(
                chat_id=os.environ['ADMIN_2_ID'],
                text=text,
                reply_markup=mk
            )
        except Exception as e:
            pass

        return 'Success', 200
    return 'Invalid method', 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
