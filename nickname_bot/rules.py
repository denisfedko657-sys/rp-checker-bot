from loaders import (
    UKRAINIAN_NAMES,
    UKRAINIAN_SURNAMES,
    RUSSIAN_NAMES,
    DIMINUTIVES,
    BANNED,
)


def check_nickname(nickname: str):
    nickname = nickname.strip()

    parts = nickname.split()

    if len(parts) != 2:
        return False, "❌ Нік має бути у форматі: Ім'я Прізвище"

    name = parts[0]
    surname = parts[1]

    # Заборонені слова
    if name.lower() in BANNED or surname.lower() in BANNED:
        return False, "❌ Нік містить заборонені слова"

    # Російські імена
    if name in RUSSIAN_NAMES:
        return False, "❌ Російське ім'я"

    # Зменшувальні
    if name in DIMINUTIVES:
        return False, "❌ Використана зменшувальна форма"

    # Якщо бази вже наповнені
    if UKRAINIAN_NAMES and name not in UKRAINIAN_NAMES:
        return False, "❌ Ім'я не знайдено в українській базі"

    if UKRAINIAN_SURNAMES and surname not in UKRAINIAN_SURNAMES:
        return False, "⚠️ Прізвище не знайдено. Потрібна ручна перевірка."

    return True, "✅ Нік пройшов перевірку."
