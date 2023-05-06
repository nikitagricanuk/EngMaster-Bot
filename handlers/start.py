from aiogram import Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.fsm.context import FSMContext

from aiogram.dispatcher.filters import Command, Text
from aiogram import F

from keyboards.kb import create_kb, start_kb_list

router = Router()
router.message.filter(F.chat.type.in_({'private'}))

@router.message(Command(commands=['start']))
async def start_cmd(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f'Приветствуем тебя, {message.from_user.first_name}!',
        reply_markup=create_kb(start_kb_list)
    )
    await state.set_state()

@router.message(Text(text='О боте'))
async def about_bot(message: Message):
    await message.answer(
'''
❓ Что такое <b>ENGMASTER BOT?</b>

С помощью этого бота вы сможете улучшить свой словарный запас английского языка.
'''
    )
