mport asyncio
import re
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot("8459389604:AAHfjNynnxJeyyty7RvLuPkJB5j7vkTwhc0")
dp = Dispatcher()


# Заборонені слова
bad_words = [
    "smith", "johnson", "jackson",
    "killer", "shadow", "dragon",
    "admin", "owner", "boss",
    "228", "1337"
]


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Напиши NickName для перевірки RP.\n\n"
        "Приклад: Денис Дасслер"
    )


@dp.message()
async def check(message: Message):
    nickname = message.text.strip()
    lower = nickname.lower()

    # Перевірка заборонених слів
    for word in bad_words:
        if word in lower:
            await message.answer(
                f"❌ {nickname}\n"
                "Не RP\n"
                "Причина: заборонене слово або іноземний нік"
            )
            return

    # Формат Ім'я Прізвище
    if not re.fullmatch(
        r"[А-ЯІЇЄҐ][а-яіїєґ]+\s[А-ЯІЇЄҐ][а-яіїєґ]+",
        nickname
    ):
        await message.answer(
            f"❌ {nickname}\n"
            "Не RP\n"
            "Причина: неправильний формат"
        )
        return


    await message.answer(
        f"✅ {nickname}\n"
        "RP NickName"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
