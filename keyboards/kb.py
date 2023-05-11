from typing import List
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_kb(kb_list: List) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True
    )

start_kb_list = [
    [KeyboardButton(text='Начать!')],
    [KeyboardButton(text='О боте')]
]

def create_exercise_kb(word):
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=f'{word[1][0]}', callback_data=f'{word[1][1]}'),
        InlineKeyboardButton(text=f'{word[2][0]}', callback_data=f'{word[2][1]}')).row(
        InlineKeyboardButton(text=f'{word[3][0]}', callback_data=f'{word[3][1]}'),
        InlineKeyboardButton(text=f'{word[4][0]}', callback_data=f'{word[4][1]}')).row(
        InlineKeyboardButton(text='Остановить сессию', callback_data='stop'))
