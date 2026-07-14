import asyncio
import re

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


bot = Bot("8459389604:AAHfjNynnxJeyyty7RvLuPkJB5j7vkTwhc0")
dp = Dispatcher()


bad_words = [
    "admin",
    "owner",
    "killer",
    "shadow",
    "dragon",
    "boss",
    "228",
    "1337"
]


foreign_surnames = [
    "Сміт",
    "Джонсон",
    "Браун",
    "Міллер",
    "Вілсон",
    "Шмідт",
    "Мюллер",
    "Гарсія",
    "Россі"
]


ukrainian_surnames = [
    "Шевченко",
    "Коваль",
    "Мельник",
    "Бондар",
    "Петренко",
    "Кравченко"
]


short_names = [
    "Саша",
    "Сашко",
    "Женя",
    "Жека",
    "Діма",
    "Дімон",
    "Коля",
    "Ваня"
]



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Введіть NickName для перевірки.\n\n"
        "Приклад:\n"
        "Олександр Коваль"
    )



@dp.message()
async def check(message: Message):

    nick = message.text.strip()
    parts = nick.split()

    # цифри
    if re.search(r"[0-9]", nick):
        await message.answer(
            f"🔴 {nick}\n\n"
            "Не RP.\n"
            "Причина: цифри у NickName."
        )
        return


    # англійські символи
    if re.search("[A-Za-z]", nick):
        await message.answer(
            f"🔴 {nick}\n\n"
            "Не RP.\n"
            "Причина: використані латинські символи."
        )
        return


    # погані слова
    for word in bad_words:
        if word.lower() in nick.lower():
            await message.answer(
                f"🔴 {nick}\n\n"
                "Не RP.\n"
                "Причина: схоже на ігровий нік."
            )
            return



    if len(parts) != 2:
        await message.answer(
            f"🟡 {nick}\n\n"
            "Потрібна RP-біографія.\n"
            "Причина: неправильний формат."
        )
        return


    name, surname = parts


    # ласкаві імена
    if name in short_names:
        await message.answer(
            f"🟢 {nick}\n\n"
            "RP.\n"
            "Ласкальна форма імені дозволена."
        )
        return


    # іноземні
    if surname in foreign_surnames:
        await message.answer(
            f"🟡 {nick}\n\n"
            "Потрібна RP-біографія.\n\n"
            "Причина: іноземне походження персонажа."
        )
        return



    # українські
    if surname in ukrainian_surnames:
        await message.answer(
            f"🟢 {nick}\n\n"
            "NickName підходить для RP."
        )
        return



    # невідомі, але схожі на реальні
    if (
        len(name) >= 3
        and len(surname) >= 4
        and name[0].isupper()
        and surname[0].isupper()
    ):
        await message.answer(
            f"🟡 {nick}\n\n"
            "Потрібна RP-біографія.\n\n"
            "Причина: невідоме походження персонажа."
        )
        return



    await message.answer(
        f"🔴 {nick}\n\n"
        "Не RP."
    )



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
