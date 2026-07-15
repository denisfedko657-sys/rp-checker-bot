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

UKRAINIAN_SURNAME_ENDINGS = (
    "енко",
    "ук",
    "юк",
    "чук",
    "чак",
    "як",
    "ак",
    "ський",
    "цький",
    "евич",
    "ович",
    "ич",
    "ко",
    "ів",
    "їв",
    "ишин",
)


def surname_check(surname: str):
    surname = surname.lower()

    if surname.lower() in {x.lower() for x in UKRAINIAN_SURNAMES}:
        return "ok"

    for ending in UKRAINIAN_SURNAME_ENDINGS:
        if surname.endswith(ending):
            return "manual"

    return "bad"


def check_nickname(nickname: str):
    nickname = nickname.strip()

    parts = nickname.split()

    if len(parts) != 2:
        return False, "❌ Нік повинен бути у форматі: Ім'я Прізвище"

    name = parts[0]
    surname = parts[1]

    name_lower = name.lower()
    surname_lower = surname.lower()

    # Заборонені слова
    if (
        name_lower in {x.lower() for x in BANNED}
        or surname_lower in {x.lower() for x in BANNED}
    ):
        return False, "❌ Містить заборонені слова."

    # Російські імена
    if name in RUSSIAN_NAMES:
        return False, "❌ Російське ім'я."

    # Зменшувальні
    if name in DIMINUTIVES:
        return False, "❌ Зменшувальна форма імені."

    # Політики
    if (
        name_lower in {x.lower() for x in POLITICIANS}
        or surname_lower in {x.lower() for x in POLITICIANS}
    ):
        return False, "❌ Заборонено використовувати прізвища політиків."

    # Блогери
    if (
        name_lower in {x.lower() for x in BLOGGERS}
        or surname_lower in {x.lower() for x in BLOGGERS}
    ):
        return False, "❌ Заборонено використовувати імена блогерів."

    # Адміністрація
    if (
        name_lower in {x.lower() for x in ADMINS}
        or surname_lower in {x.lower() for x in ADMINS}
    ):
        return False, "❌ Заборонено використовувати ніки адміністрації."

    # Об'єкти
    if (
        name_lower in {x.lower() for x in OBJECTS}
        or surname_lower in {x.lower() for x in OBJECTS}
    ):
        return False, "❌ Не можна використовувати назви предметів."

    # Проєкти
    if (
        name_lower in {x.lower() for x in PROJECTS}
        or surname_lower in {x.lower() for x in PROJECTS}
    ):
        return False, "❌ Не можна використовувати назви проєктів."

    # Українське ім'я
    if UKRAINIAN_NAMES:
        if name not in UKRAINIAN_NAMES:
            return False, "❌ Ім'я відсутнє в українській базі."

    # Перевірка прізвища
    result = surname_check(surname)

    if result == "ok":
        return True, "✅ Нік відповідає правилам."

    if result == "manual":
        return False, "⚠️ Рідкісне прізвище. Потрібна ручна перевірка."

    return False, "❌ Прізвище не схоже на українське."
