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
    await message.answer(f"Assalawmagaleykum {message.from_user.first_name} \nXosh kelibsiz \n /settings - Sazlamalar \n /channels -Kanallar")


@dp.message(Command('settings'))
async def settings(message:Message):
    await message.answer(f"Sazlamalar")

@dp.message(Command('channels'))
async def channels(message:Message):
    await message.answer(f"Kanallar")

@dp.message(Command('tel'))
async def tel(message:Message):
    await message.answer(f"Sorawlar boyinsha tomendegi nomerge xabarlassaniz boladi. \n+998997654321")

@dp.message(Command('help'))
async def help(message:Message):
    await message.answer(f"Can I help you?")
 
@dp.message(Command('info'))
async def channels(message:Message):
    await message.answer(f"Bot haqqinda informatsiya biliwdi qaleysizba?")

@dp.message(Command('ofis'))
async def channels(message:Message):
    await message.answer(f"Qaraqalpaqstan koshe")

@dp.message(Command('job'))
async def channels(message:Message):
    await message.answer(f"Jimis")


async def main():
    print('bot iske qosildi..')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())