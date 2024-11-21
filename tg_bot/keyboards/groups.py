from os import getenv

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tg_bot.lexicon.buttons import lexicon as btns_lexicon
from tg_bot.lexicon.messages import lexicon as msgs_lexicon


def get_groups_names_kb(groups_list: list) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    for group in groups_list:
        builder.row(
            KeyboardButton(text=group['name'])
        )

    return builder.as_markup(resize_keyboard=True)
