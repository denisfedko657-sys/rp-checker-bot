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


def check_nickname(nickname: str):
    nickname = nickname.strip()

    parts = nickname.split()

    if len(parts) != 2:
        return False, "❌ Нік має бути у форматі: Ім'я Прізвище"

    name = parts[0]
    surname = parts[1]

    name_lower = name.lower()
    surname_lower = surname.lower()

    # Заборонені слова
    if name_lower in BANNED or surname_lower in BANNED:
        return False, "❌ Нік містить заборонені слова."

    # Російські імена
    if name in RUSSIAN_NAMES:
        return False, "❌ Російське ім'я."

    # Зменшувальні форми
    if name in DIMINUTIVES:
        return False, "❌ Використана зменшувальна форма імені."

    # Політики
    if (
        name_lower in POLITICIANS
        or surname_lower in POLITICIANS
    ):
        return False, "❌ Заборонено використовувати прізвища політиків."

    # Блогери
    if (
        name_lower in BLOGGERS
        or surname_lower in BLOGGERS
    ):
        return False, "❌ Заборонено використовувати імена блогерів."

    # Адміністрація
    if (
        name_lower in ADMINS
        or surname_lower in ADMINS
    ):
        return False, "❌ Заборонено використовувати ніки адміністрації."

    # Об'єкти
    if (
        name_lower in OBJECTS
        or surname_lower in OBJECTS
    ):
        return False, "❌ Не можна використовувати назви предметів."

    # Проєкти
    if (
        name_lower in PROJECTS
        or surname_lower in PROJECTS
    ):
        return False, "❌ Не можна використовувати назви проєктів."

    # Українські імена
    if UKRAINIAN_NAMES:
        if name not in UKRAINIAN_NAMES:
            return False, "❌ Українське ім'я не знайдено в базі."

    # Українські прізвища
    if UKRAINIAN_SURNAMES:
        if surname not in UKRAINIAN_SURNAMES:
            return (
                False,
                "⚠️ Прізвище не знайдено в базі. Потрібна ручна перевірка."
            )

    return True, "✅ Нік відповідає правилам UG."
