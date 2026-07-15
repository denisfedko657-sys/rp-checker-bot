import re

from database import (
    RUSSIAN_LETTERS,
    DIMINUTIVES,
    BAD_WORDS,
    RUSSIAN_NAMES
)


def check_nickname(nickname: str):

    errors = []

    nickname = nickname.strip()

    # 3.1 Формат "Ім'я Прізвище"

    parts = nickname.split()

    if len(parts) != 2:
        errors.append("Нікнейм повинен бути у форматі «Ім'я Прізвище».")
        return False, errors

    name, surname = parts

    # Перша літера велика

    if not name[0].isupper() or not surname[0].isupper():
        errors.append("Ім'я та прізвище повинні починатися з великої літери.")

    # Решта маленькі

    if name[1:] != name[1:].lower():
        errors.append("В імені всі літери після першої повинні бути малими.")

    if surname[1:] != surname[1:].lower():
        errors.append("У прізвищі всі літери після першої повинні бути малими.")

    # Лише українська кирилиця

    if not re.fullmatch(r"[А-ЯІЇЄҐа-яіїєґ']+\s[А-ЯІЇЄҐа-яіїєґ']+", nickname):
        errors.append("Дозволена тільки українська кирилиця.")

    # Російські літери

    for ch in nickname.lower():
        if ch in RUSSIAN_LETTERS:
            errors.append("Виявлено російські літери.")
            break

    # Цифри

    if re.search(r"\d", nickname):
        errors.append("Заборонено використовувати цифри.")

    # Символи

    if re.search(r"[^А-ЯІЇЄҐа-яіїєґ' ]", nickname):
        errors.append("Заборонені сторонні символи.")

    # Російські імена

    if name in RUSSIAN_NAMES:
        errors.append("Використано російськомовне ім'я.")

    # Заборонені слова

    text = nickname.lower()

    for word in BAD_WORDS:
        if word in text:
            errors.append(f'Заборонене слово: "{word}".')
            break

    # Пестливі форми

    for end in DIMINUTIVES:

        if name.lower().endswith(end):
            errors.append("Ім'я має пестливу форму.")
            break

    # Набір букв

    vowels = "аеєиіїоуюя"

    if sum(c in vowels for c in name.lower()) == 0:
        errors.append("Ім'я схоже на набір букв.")

    if sum(c in vowels for c in surname.lower()) == 0:
        errors.append("Прізвище схоже на набір букв.")

    if errors:
        return False, errors

    return True, ["NickName відповідає правилам."]
