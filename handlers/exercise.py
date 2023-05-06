from aiogram import Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InlineKeyboardButton

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.fsm.context import FSMContext
#from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command, Text
from aiogram import F

from aiogram.utils.keyboard import InlineKeyboardBuilder
#from aiogram.types.inline_keyboard import InlineKeyboardMarkup

from keyboards.kb import create_kb, start_kb_list

from words import words
from random import randint as rint


async def send_exercise(callback: CallbackQuery, state: FSMContext):
    word = words[rint(0, 200)]
    await state.update_data(word=word)
    ikb = InlineKeyboardBuilder().row(InlineKeyboardButton(text=f'{word[1][0]}', callback_data=f'{word[1][1]}'), InlineKeyboardButton(text=f'{word[2][0]}', callback_data=f'{word[2][1]}')).row(InlineKeyboardButton(
        text=f'{word[3][0]}', callback_data=f'{word[3][1]}'), InlineKeyboardButton(text=f'{word[4][0]}', callback_data=f'{word[4][1]}')).row(InlineKeyboardButton(text='Остановить сессию', callback_data='stop'))
    await callback.message.edit_text(f'<b>{word[0]} — ...</b>', reply_markup=ikb.as_markup())


class Exercisig(StatesGroup):
    lobby = State()
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
    await state.set_state(Exercisig.exercise)
    await state.update_data(words_num=0, rights=0)
    word = words[rint(0, 200)]
    await state.update_data(word=word)
    ikb = InlineKeyboardBuilder().row(InlineKeyboardButton(text=f'{word[1][0]}', callback_data=f'{word[1][1]}'), InlineKeyboardButton(text=f'{word[2][0]}', callback_data=f'{word[2][1]}')).row(InlineKeyboardButton(
        text=f'{word[3][0]}', callback_data=f'{word[3][1]}'), InlineKeyboardButton(text=f'{word[4][0]}', callback_data=f'{word[4][1]}')).row(InlineKeyboardButton(text='Остановить сессию', callback_data='stop'))
    await message.answer('Сессия началась! Вы можете в любой момент закончить её нажатием кнопки на клавиатуре и узнать свои результаты', reply_markup=ReplyKeyboardRemove())
    await message.answer(f'<b>{word[0]} — ...</b>', reply_markup=ikb.as_markup())


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
''', reply_markup=create_kb(start_kb_list))
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
