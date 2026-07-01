import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from dotenv import load_dotenv
import os
load_dotenv()

Token = os.getenv("API")
dp = Dispatcher()
bot = Bot(token=Token)

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f"Assalawmagaleykum {message.from_user.first_name} \nXosh kelibsiz")

@dp.message(Command())
async def settings(message:Message):
    await message.answer(f"Sazlamalar")

@dp.message(Command())
async def channels(message:Message):
    await message.answer(f"Kanallar")

async def main():
    print('bot iske qosildi..')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())