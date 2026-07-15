import re

from loaders import (
    UKRAINIAN_NAMES,
    UKRAINIAN_SURNAMES,
    RUSSIAN_NAMES,
    DIMINUTIVES,
    BANNED,
    POLITICIANS,
    BLOGGERS,
    OBJECTS,
    PROJECTS,
    ADMINS,
)

SURNAME_ENDINGS = (
    "енко", "ук", "юк", "чук", "чак",
    "ський", "цький", "евич", "ович",
    "ко", "ак", "як", "ич", "ів", "їв"
)


def check_nickname(nickname: str):

    nickname = nickname.strip()

    parts = nickname.split()

    if len(parts) != 2:
        return False, "❌ Нік має бути у форматі Ім'я Прізвище."

    name = parts[0]
    surname = parts[1]

    # тільки українські літери
    if not re.fullmatch(r"[А-ЯІЇЄҐа-яіїєґ'-]+", name):
        return False, "❌ Ім'я містить недопустимі символи."

    if not re.fullmatch(r"[А-ЯІЇЄҐа-яіїєґ'-]+", surname):
        return False, "❌ Прізвище містить недопустимі символи."

    name_l = name.lower()
    surname_l = surname.lower()

    banned = {x.lower() for x in BANNED}

    if name_l in banned or surname_l in banned:
        return False, "❌ Заборонене слово."

    if name in RUSSIAN_NAMES:
        return False, "❌ Російське ім'я."

    if name in DIMINUTIVES:
        return False, "❌ Зменшувальна форма."

    if name_l in {x.lower() for x in POLITICIANS}:
        return False, "❌ Ім'я політика."

    if surname_l in {x.lower() for x in POLITICIANS}:
        return False, "❌ Прізвище політика."

    if name_l in {x.lower() for x in BLOGGERS}:
        return False, "❌ Ім'я блогера."

    if surname_l in {x.lower() for x in BLOGGERS}:
        return False, "❌ Прізвище блогера."

    if name_l in {x.lower() for x in ADMINS}:
        return False, "❌ Ім'я адміністрації."

    if surname_l in {x.lower() for x in ADMINS}:
        return False, "❌ Прізвище адміністрації."

    if name_l in {x.lower() for x in OBJECTS}:
        return False, "❌ Назва предмета."

    if surname_l in {x.lower() for x in OBJECTS}:
        return False, "❌ Назва предмета."

    if name_l in {x.lower() for x in PROJECTS}:
        return False, "❌ Назва проєкту."

    if surname_l in {x.lower() for x in PROJECTS}:
        return False, "❌ Назва проєкту."

    if UKRAINIAN_NAMES:
        if name not in UKRAINIAN_NAMES:
            return False, "⚠️ Ім'я відсутнє в базі."

    if UKRAINIAN_SURNAMES:
        if surname in UKRAINIAN_SURNAMES:
            return True, "✅ Нік дозволений."

    for ending in SURNAME_ENDINGS:
        if surname_l.endswith(ending):
            return False, "⚠️ Рідкісне прізвище. Потрібна ручна перевірка."

    return False, "❌ Прізвище не схоже на українське."
