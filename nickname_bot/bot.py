from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F

from config import BOT_TOKEN
from validator import validate_format

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Вітаю!\n\nНадішли мені нікнейм у форматі:\n\nІм'я Прізвище"
    )


@dp.message(F.text)
async def check(message: Message):

    if validate_format(message.text):
        await message.answer("✅ Формат правильний")
    else:
        await message.answer("❌ Неправильний формат")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
