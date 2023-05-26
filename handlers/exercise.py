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

# , DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT
from config import WORD_TYPES
from databases.db import connect_db


async def send_exercise(callback: CallbackQuery, state: FSMContext):
    word = words[rint(0, 200)]
    await state.update_data(word=word)
    ikb = InlineKeyboardBuilder().row(InlineKeyboardButton(text=f'{word[1][0]}', callback_data=f'{word[1][1]}'), InlineKeyboardButton(text=f'{word[2][0]}', callback_data=f'{word[2][1]}')).row(InlineKeyboardButton(
        text=f'{word[3][0]}', callback_data=f'{word[3][1]}'), InlineKeyboardButton(text=f'{word[4][0]}', callback_data=f'{word[4][1]}')).row(InlineKeyboardButton(text='Остановить сессию', callback_data='stop'))
    await callback.message.edit_text(f'<b>{word[0]} — ...</b>', reply_markup=ikb.as_markup())


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
    await new_exercise(callback, state, 'A1')


@router.callback_query(Exercisig.choose_level, text='A2')
async def start_exercise_A2(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await new_exercise(callback, state, 'A2')


@router.callback_query(Exercisig.choose_level, text='B1')
async def start_exercise_B1(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await new_exercise(callback, state, 'B1')


@router.callback_query(Exercisig.choose_level, text='B2')
async def start_exercise_B2(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await new_exercise(callback, state, 'B2')


@router.callback_query(Exercisig.choose_level, text='C1')
async def start_exercise_C1(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await new_exercise(callback, state, 'C1')


@router.callback_query(Exercisig.exercise, text='stop')
async def stop_session(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Exercisig.lobby)
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


async def new_exercise(callback, state, level):
    await state.set_state(Exercisig.exercise)

    kind = random.choice(WORD_TYPES)
    word = new_word(level, kind, rint(0, get_number_of_words(level, kind)))

    await state.update_data(words_num=0, rights=0)
    await state.update_data(word=word)

    await callback.message.answer('Сессия началась! Вы можете в любой момент закончить её нажатием кнопки на клавиатуре и узнать свои результаты', reply_markup=ReplyKeyboardRemove())
    await callback.message.answer(f'<b>{word[0]} — ...</b>', reply_markup=create_exercise_kb(word).as_markup())


def new_word(level, kind, id):
    db_connection = connect_db()
    cursor = db_connection.cursor()

    cursor.execute(f'SELECT * FROM words_{level}_{kind} WHERE id = {id}')
    data = cursor.fetchall()

    print(data)


def get_number_of_words(level, kind):
    db_connection = connect_db()
    cursor = db_connection.cursor()

    cursor.execute(f'SELECT * FROM words_{level}_{kind}')

    return cursor.rowcount
