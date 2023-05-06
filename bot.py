import asyncio
import logging
from aiogram import Bot, Dispatcher

from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
#from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

from handlers import exercise
#from middlewares.weekend import WeekendCallbackMiddleware

logging.basicConfig(level=logging.INFO,
                    format='%(filename)s - [%(asctime)s] - %(levelname)s - %(name)s - %(message)s')

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(storage=MemoryStorage())


async def main():
    # dp.include_router(start.router)
    dp.include_router(exercise.router)
    # dp.callback_query.outer_middleware(WeekendCallbackMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
