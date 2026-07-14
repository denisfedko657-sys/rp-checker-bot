import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import "8459389604:AAHfjNynnxJeyyty7RvLuPkJB5j7vkTwhc0"

bot = Bot("8459389604:AAHfjNynnxJeyyty7RvLuPkJB5j7vkTwhc0")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Вітаю!\n\n"
        "Надішли мені RP NickName для перевірки.\n\n"
        "Наприклад:\n"
        "Денис Дасслер"
    )


@dp.message()
async def check(message: Message):
    await message.answer(f"🔍 Перевіряю:\n{message.text}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
