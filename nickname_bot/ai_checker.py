import json
import urllib.request


def ai_check_nickname(name, surname):

    prompt = f"""
Перевір український нік.

Ім'я: {name}
Прізвище: {surname}

Визнач:
1. Чи може це бути справжнє українське ім'я та прізвище.
2. Чи схоже прізвище на українське.
3. Чи є це відомою людиною, організацією або предметом.

Відповідь тільки JSON:

{{
"allowed": true/false,
"reason": "коротка причина"
}}
"""

    # тут буде підключення ШІ
    # поки тестовий режим

    ukrainian_endings = (
        "енко",
        "ук",
        "юк",
        "чук",
        "ський",
        "цький",
        "евич",
        "ович"
    )

    surname = surname.lower()

    for end in ukrainian_endings:
        if surname.endswith(end):
            return {
                "allowed": True,
                "reason": "Схоже на українське прізвище"
            }

    return {
        "allowed": False,
        "reason": "ШІ не зміг підтвердити українське походження"
    }
