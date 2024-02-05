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
    [KeyboardButton(text='Мои слова')],
    [KeyboardButton(text='О боте')]
]

def create_exercise_kb(word):
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text=f'{word[1][0]}', callback_data=f'{word[1][1]}'),
        InlineKeyboardButton(text=f'{word[2][0]}', callback_data=f'{word[2][1]}')).row(
        InlineKeyboardButton(text=f'{word[3][0]}', callback_data=f'{word[3][1]}'),
        InlineKeyboardButton(text=f'{word[4][0]}', callback_data=f'{word[4][1]}')).row(
        InlineKeyboardButton(text='Остановить сессию', callback_data='stop'))

def create_level_kb():
    return InlineKeyboardBuilder().row(
        InlineKeyboardButton(text='A1', callback_data='A1'),
        InlineKeyboardButton(text='A2', callback_data='A2')).row(
        InlineKeyboardButton(text='B1', callback_data='B1'),
        InlineKeyboardButton(text='B2', callback_data='B2')).row(
        InlineKeyboardButton(text='C1', callback_data='C1'))
