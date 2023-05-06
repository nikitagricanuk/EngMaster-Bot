from typing import List
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup


def create_kb(kb_list: List) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True
    )


start_kb_list = [
    [KeyboardButton(text='Начать!')],
    [KeyboardButton(text='О боте')]
]
