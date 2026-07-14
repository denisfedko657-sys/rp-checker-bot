import asyncio
import re

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


bot = Bot("8459389604:AAHfjNynnxJeyyty7RvLuPkJB5j7vkTwhc0")
dp = Dispatcher()


# Українські імена
ukraine_names = {
    "Олег","Денис","Іван","Петро","Андрій",
    "Максим","Олександр","Владислав","Микола",
    "Сергій","Роман","Богдан","Дмитро",
    "Тарас","Василь","Юрій","Віталій",
    "Артур","Антон","Євген"
}


# Українські прізвища
ukraine_surnames = {
    "Коваль","Шевченко","Бондар","Мельник",
    "Петренко","Кравченко","Ткаченко",
    "Поліщук","Лисенко","Олійник",
    "Савченко","Даниленко","Іванов",
    "Дасслер"
}


# Іноземні (українською)
foreign_surnames = {
    "Сміт","Джонсон","Вільямс",
    "Браун","Міллер","Вілсон",
    "Тейлор","Андерсон","Томпсон",
    "Девіс","Мартін","Кларк",
    "Льюїс","Вокер","Холл"
}


foreign_names = {
    "Майкл","Джон","Роберт",
    "Девід","Кріс","Джеймс",
    "Вільям","Томас"
}


bad_words = {
    "admin","owner","killer",
    "shadow","dragon","228",
    "mafia","boss"
}



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Надішли RP NickName.\n\n"
        "Приклад:\n"
        "Олег Коваль"
    )



@dp.message()
async def check(message: Message):

    nick = message.text.strip()
    parts = nick.split()

    low = nick.lower()


    # цифри та символи
    if re.search(r"[0-9_]", nick):
        await message.answer(
            f"❌ {nick}\n\n"
            "Не RP.\n"
            "Причина: цифри або символи в NickName."
        )
        return


    # заборонені слова
    for word in bad_words:
        if word in low:
            await message.answer(
                f"❌ {nick}\n\n"
                "Не RP.\n"
                "Причина: ігровий нік."
            )
            return


    if len(parts) != 2:
        await message.answer(
            f"❌ {nick}\n\n"
            "Не RP.\n"
            "Формат має бути: Ім'я Прізвище."
        )
        return


    name, surname = parts


    # іноземні
    if name in foreign_names or surname in foreign_surnames:
        await message.answer(
            f"⚠️ {nick}\n\n"
            "Потрібна RP-біографія.\n\n"
            "Причина: іноземне ім'я або прізвище."
        )
        return


    # українські
    if name in ukraine_names and surname in ukraine_surnames:
        await message.answer(
            f"✅ {nick}\n\n"
            "NickName підходить для RP."
        )
        return


    # все інше
    await message.answer(
        f"❌ {nick}\n\n"
        "Не RP.\n\n"
        "Причина: невідоме ім'я або прізвище.\n"
        "Потрібно створити RP-біографію персонажа."
    )



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
