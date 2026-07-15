import re

nickname_pattern = re.compile(r"^[А-ЯІЇЄҐ][а-яіїєґ']+\s[А-ЯІЇЄҐ][а-яіїєґ'-]+$")


def validate_format(text: str):
    return bool(nickname_pattern.match(text))
