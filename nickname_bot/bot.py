from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN
from validator import validate_format
from rules import check_nickname

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Вітаю!\n\n"
        "Надішли нікнейм у форматі:\n"
        "Ім'я Прізвище"
    )


@dp.message(F.text)
async def check(message: Message):
    nickname = message.text.strip()

    if not validate_format(nickname):
        await message.answer("❌ Неправильний формат.\n\nПриклад: Олег Шевченко")
        return

    status, response = check_nickname(nickname)
    await message.answer(response)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
