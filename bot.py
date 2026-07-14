import asyncio
import re

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


bot = Bot("8459389604:AAHfjNynnxJeyyty7RvLuPkJB5j7vkTwhc0")
dp = Dispatcher()


bad_words = [
    "хуй", "хуесос", "бля", "блядь",
    "сука", "єб", "еб", "пізд",
    "мудак", "лох", "дебіл",
    "admin", "owner", "killer",
    "shadow", "dragon", "boss"
]


foreign_names = [
    "Майкл", "Джон", "Роберт",
    "Джеймс", "Вільям", "Девід"
]


foreign_surnames = [
    "Сміт", "Джонсон",
    "Браун", "Міллер",
    "Вілсон", "Шмідт",
    "Мюллер", "Гарсія"
]


short_names = [
    "Саша", "Сашко",
    "Женя", "Жека",
    "Діма", "Дімон",
    "Коля", "Ваня",
    "Льоша"
]


def calculate_rp(name, surname):

    score = 0


    text = name + surname


    # правильний формат
    if len(name) >= 3 and len(surname) >= 4:
        score += 15


    # великі букви
    if name[0].isupper() and surname[0].isupper():
        score += 10


    # тільки українські букви
    if re.fullmatch("[А-ЯІЇЄҐа-яіїєґ]+", text):
        score += 20


    # голосні (щоб не було абвгд)
    vowels = "аеєиіїоуюя"

    if sum(1 for x in name.lower() if x in vowels) >= 2:
        score += 15

    if sum(1 for x in surname.lower() if x in vowels) >= 2:
        score += 15


    # закінчення прізвища
    if surname.endswith(
        (
            "енко",
            "ук",
            "юк",
            "чук",
            "ко",
            "ський",
            "цький",
            "ов",
            "ев",
            "ич"
        )
    ):
        score += 15


    # ласкаве ім'я
    if name in short_names:
        score += 5


    # іноземні
    if name in foreign_names or surname in foreign_surnames:
        score -= 15


    # мати
    for word in bad_words:
        if word in text.lower():
            score -= 70


    # цифри
    if re.search(r"[0-9]", text):
        score -= 50


    if score < 0:
        score = 0

    if score > 100:
        score = 100


    return score



@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "👋 Введи NickName для перевірки.\n\n"
        "Приклад:\n"
        "Олег Шевченко"
    )



@dp.message()
async def check(message: Message):

    nick = message.text.strip()
    parts = nick.split()


    if len(parts) != 2:
        await message.answer(
            "❌ Формат неправильний.\n"
            "Потрібно: Ім'я Прізвище"
        )
        return


    name, surname = parts


    percent = calculate_rp(name, surname)



    if percent >= 85:

        status = "🟢 RP підходить"

    elif percent >= 50:

        status = "🟡 Потрібна RP-біографія"

    else:

        status = "🔴 Не RP"



    await message.answer(
        f"🔎 Перевірка: {nick}\n\n"
        f"RP-рейтинг: {percent}%\n\n"
        f"Статус: {status}"
    )



async def main():

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
