from aiogram import Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InlineKeyboardButton

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.fsm.context import FSMContext
# from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command, Text
from aiogram import F

from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.types.inline_keyboard import InlineKeyboardMarkup

from keyboards.kb import create_kb, start_kb_list, create_exercise_kb, create_level_kb

from words import words
import random
from random import randint as rint

import logging

# , DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT
from config import WORD_TYPES
from databases.db import connect_db

level = None

async def send_exercise(callback: CallbackQuery, state: FSMContext):
    kind = random.choice(WORD_TYPES)
    word = new_word(kind, rint(0, get_number_of_words(kind)))
    await state.update_data(word=word)
    ikb = InlineKeyboardBuilder().row(InlineKeyboardButton(text=f'{word[1][0]}', callback_data=f'{word[1][1]}'), InlineKeyboardButton(text=f'{word[2][0]}', callback_data=f'{word[2][1]}')).row(InlineKeyboardButton(
        text=f'{word[3][0]}', callback_data=f'{word[3][1]}'), InlineKeyboardButton(text=f'{word[4][0]}', callback_data=f'{word[4][1]}')).row(InlineKeyboardButton(text='Остановить сессию', callback_data='stop'))
    await callback.message.edit_text(f'<b>{word[0][0]} — ...</b>', reply_markup=ikb.as_markup())


class Exercisig(StatesGroup):
    lobby = State()
    choose_level = State()
    exercise = State()


router = Router()
router.message.filter(F.chat.type.in_({'private'}))


@router.message(Command(commands=['start']))
async def start_cmd(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f'Приветствуем тебя, {message.from_user.first_name}!',
        reply_markup=create_kb(start_kb_list)
    )
    await state.set_state(Exercisig.lobby)


@router.message(Text(text='О боте'))
async def about_bot(message: Message):
    await message.answer(
        '''
            ❓ Что такое <b>ENGMASTER BOT?</b>

            С помощью этого бота вы сможете улучшить свой словарный запас английского языка.
        '''
    )


@router.message(Exercisig.lobby, Text(text='Начать!'))
async def start_session(message: Message, state: FSMContext):
    await state.set_state(Exercisig.choose_level)
    await message.answer('Для начала, за какой уровень английского слова ты хотел бы выучить?', reply_markup=create_level_kb().as_markup())


@router.callback_query(Exercisig.choose_level, text='A1')
async def start_exercise_A1(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    level = 'a1'
    await new_exercise(callback, state)


@router.callback_query(Exercisig.choose_level, text='A2')
async def start_exercise_A2(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    level = 'a2'
    await new_exercise(callback, state)


@router.callback_query(Exercisig.choose_level, text='B1')
async def start_exercise_B1(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    level = 'b1'
    await new_exercise(callback, state)


@router.callback_query(Exercisig.choose_level, text='B2')
async def start_exercise_B2(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    level = 'b2'
    await new_exercise(callback, state)


@router.callback_query(Exercisig.choose_level, text='C1')
async def start_exercise_C1(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    level = 'c1'
    await new_exercise(callback, state)


@router.callback_query(Exercisig.exercise, text='stop')
async def stop_session(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Exercisig.lobby)
    level = None
    data = await state.get_data()
    words_num = data.get('words_num')
    rights = data.get('rights')
    await callback.message.edit_text('Сессия завершена!')
    if words_num == 0:
        await callback.message.answer(
            '''
                <b>Результаты</b>

                Всего слов: 0
            ''',
            reply_markup=create_kb(start_kb_list))

    else:
        await callback.message.answer(
            f'''
            <b>Результаты</b>

            Всего слов: {words_num}
            Всего правильных ответов: {rights}
            Всего неправильных ответов: {words_num-rights}

            <b>{round((rights*100)/words_num, 1)}% ваших ответов являются правильными!</b>
            ''',
            reply_markup=create_kb(start_kb_list))


@router.callback_query(Exercisig.exercise, text='true')
async def right_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    words_num = data.get('words_num')
    rights = data.get('rights')

    await state.update_data(words_num=words_num+1, rights=rights+1)
    await callback.answer('✅ Верно!')
    await send_exercise(callback, state)


@router.callback_query(Exercisig.exercise, text='false')
async def false_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    words_num = data.get('words_num')
    word = data.get('word')
    await state.update_data(words_num=words_num+1)

    await callback.answer('❌ Неверно!')
    right_trans = [right[0] for right in word if right[1] == 'true']
    await callback.message.answer(f'<b>{word[0]} — {right_trans[0]} ❗</b>')
    await send_exercise(callback, state)


async def new_exercise(callback, state):
    await state.set_state(Exercisig.exercise)

    logging.error('In new_exercise() function 1!')

    kind = random.choice(WORD_TYPES)
    word = new_word(kind, rint(0, get_number_of_words(kind)))

    await state.update_data(words_num=0, rights=0)
    await state.update_data(word=word)

    logging.error('In new_exercise() function 2!')

    await callback.message.answer('Сессия началась! Вы можете в любой момент закончить её нажатием кнопки на клавиатуре и узнать свои результаты', reply_markup=ReplyKeyboardRemove())
    await callback.message.answer(f'<b>{word[0][0]} — ...</b>', reply_markup=create_exercise_kb(word).as_markup())


def new_word(kind, id):
    db_connection = connect_db()
    cursor = db_connection.cursor()

    logging.error('In new_word() function 1!')

    cursor.execute(f'SELECT * FROM words_{level}_{kind} WHERE id = {id}')
    data = cursor.fetchall()

    logging.error('In new_word() function 2!')

    incorrect_words = []
    for i in range(3):
        incorrect_word_id = rint(0, get_number_of_words(kind))
        while incorrect_word_id == id:
            tmp = rint(0, get_number_of_words(kind))
            print(tmp)
            incorrect_word_id = tmp
        
        cursor.execute(f'SELECT * FROM words_{level}_{kind} WHERE id = {incorrect_word_id}')
        incorrent_word_translate = cursor.fetchall()
        print(f'In table words_{level}_{kind} data is', incorrent_word_translate)
        incorrect_words.append(incorrent_word_translate[0][3])

    # In this section we determine the word order.
    # Here we're randomly choose in which part of return value
    # will be true and in which false.
    # Genius hack, I know :)
    word_order = rint(0, 3)
    if word_order == 0:
        word1 = 'true'
        word2 = 'false'
        word3 = 'false'
        word4 = 'false'
    elif word_order == 1:
        word1 = 'false'
        word2 = 'true'
        word3 = 'false'
        word4 = 'false'
    elif word_order == 2:
        word1 = 'false'
        word2 = 'false'
        word3 = 'true'
        word4 = 'false'
    else:
        word1 = 'false'
        word2 = 'false'
        word3 = 'false'
        word4 = 'true'

#          [('Word', 'Transcription'), ('Translation1', 'true'),
#           ('Translation2', 'false'), ('Translation3', 'false'), 
#           ('Translation4', 'false')]
    return [(str(data[0][1]), str(data[0][2])), (str(data[0][3]), word1),
            (str(incorrect_words[0]), word2), (str(incorrect_words[1]), word3),
            (str(incorrect_words[2]), word4)] 


def get_number_of_words(kind):
    db_connection = connect_db()
    cursor = db_connection.cursor()
    logging.error('In get_number_of_words() function 1!')
    cursor.execute(f'SELECT * FROM words_{level}_{kind}')
    logging.error('In get_number_of_words() function 2!')
    return cursor.rowcount
