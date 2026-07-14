import asyncio
import re

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


bot = Bot("8459389604:AAHfjNynnxJeyyty7RvLuPkJB5j7vkTwhc0")
dp = Dispatcher()


# Ласкальні імена
short_names = {
    "Саша", "Сашко", "Шура",
    "Льоша", "Льоха",
    "Олежик",
    "Діма", "Дімон",
    "Женя", "Жека",
    "Серьожа", "Серьога",
    "Коля",
    "Ваня",
    "Петя"
}


# Відомі українські імена
names = {
    "Олександр",
    "Олексій",
    "Олег",
    "Денис",
    "Іван",
    "Петро",
    "Андрій",
    "Максим",
    "Дмитро",
    "Сергій",
    "Микола",
    "Владислав",
    "Роман",
    "Богдан",
    "Тарас",
    "Василь",
    "Юрій",
    "Віталій",
    "Антон",
    "Євген",
    "Марія",
    "Анна",
    "Олена",
    "Катерина"
}


# Прізвища, які точно RP
ukraine_surnames = {
    "Шевченко",
    "Коваль",
    "Мельник",
    "Бондар",
    "Петренко",
    "Кравченко",
    "Ткаченко",
    "Савченко",
    "Лисенко",
    "Поліщук",
    "Олійник",
    "Козак",
    "Бойко",
    "Гнатюк",
    "Даниленко"
}


# Іноземні варіанти
foreign_words = {
    "Сміт",
    "Джонсон",
    "Браун",
    "Міллер",
    "Вілсон",
    "Тейлор",
    "Андерсон",
    "Томпсон",
    "Шмідт",
    "Мюллер",
    "Гарсія",
    "Лопес",
    "Россі",
    "Майкл",
    "Джон",
    "Роберт",
    "Джеймс"
}


# Ігрові слова
bad_words = {
    "admin",
    "owner",
    "boss",
    "killer",
    "shadow",
    "dragon",
    "228",
    "1337"
}


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Надішли NickName для перевірки RP.\n\n"
        "Приклад:\n"
        "Олег Коваль"
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
            "Причина: цифри в NickName."
        )
        return


    # латиниця
    if re.search(r"[A-Za-z]", nick):
        await message.answer(
            f"🔴 {nick}\n\n"
            "Не RP.\n"
            "Причина: англійські символи."
        )
        return


    # погані слова
    for word in bad_words:
        if word in nick.lower():
            await message.answer(
                f"🔴 {nick}\n\n"
                "Не RP.\n"
                "Причина: ігровий нік."
            )
            return


    # формат
    if len(parts) != 2:
        await message.answer(
            f"🟡 {nick}\n\n"
            "Потрібна RP-біографія.\n"
            "Формат: Ім'я Прізвище"
        )
        return


    name, surname = parts


    # ласкальні імена
    if name in short_names:
        await message.answer(
            f"🟢 {nick}\n\n"
            "RP.\n"
            "Ласкальна форма імені."
        )
        return


    # іноземні
    if name in foreign_words or surname in foreign_words:
        await message.answer(
            f"🟡 {nick}\n\n"
            "Потрібна RP-біографія.\n\n"
            "Причина: іноземне походження персонажа."
        )
        return


    # українські по списку
    if name in names and surname in ukraine_surnames:
        await message.answer(
            f"🟢 {nick}\n\n"
            "NickName підходить для RP."
        )
        return


    # аналіз прізвища
    if surname.endswith(
        (
            "енко",
            "ук",
            "юк",
            "чук",
            "ко",
            "ський",
            "цький",
            "ич",
            "ов",
            "ев"
        )
    ):
        await message.answer(
            f"🟢 {nick}\n\n"
            "NickName схоже на реальне RP."
        )
        return


    # якщо невідоме
    await message.answer(
        f"🟡 {nick}\n\n"
        "Потрібна RP-біографія.\n\n"
        "Причина: невідоме походження персонажа."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())
