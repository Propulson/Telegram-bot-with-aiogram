import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


from config import token
from button import link_bt


logging.basicConfig(level=logging.INFO)
bot = Bot(token)
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")


@dp.message(Command("start"))
async def start(message: types.Message) -> None:
    """func - command start"""
    await message.answer('Hello, mi frendo!!!\n'
                         "My main task it's helping y\n"
                         "Y can write /help to see all commands")
    await message.answer('Choose link for information', reply_markup=link_bt())


@dp.message(Command("help"))
async def helps(message: types.Message) -> None:
    """func - command help"""
    await message.answer('This command is working now:\n'
                         '/start - for starting the bot\n'
                         '/info - for getting the bot info\n')


@dp.message(Command("info"))
async def info(message: types.Message, started_at: datetime = None):
    """func - command info"""
    await message.answer(f'Bot started {started_at}')


async def main() -> None:
    """func - main function"""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
