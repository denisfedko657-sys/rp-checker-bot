import re

def check_nickname(nickname: str):
    nickname = nickname.strip()

    # Формат: Ім'я Прізвище
    if not re.fullmatch(r"[A-Za-zА-ЯІЇЄҐа-яіїєґ']+\s[A-Za-zА-ЯІЇЄҐа-яіїєґ']+", nickname):
        return False, "❌ Нікнейм повинен бути у форматі: Ім'я Прізвище"

    first, last = nickname.split()

    # Велика літера
    if not first[0].isupper():
        return False, "❌ Ім'я повинно починатися з великої літери."

    if not last[0].isupper():
        return False, "❌ Прізвище повинно починатися з великої літери."

    # Не однакові
    if first.lower() == last.lower():
        return False, "❌ Ім'я та прізвище не можуть бути однаковими."

    return True, "✅ RP NickName"
