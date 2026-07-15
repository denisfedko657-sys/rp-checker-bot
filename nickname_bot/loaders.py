import json
from pathlib import Path

DATA = Path("data")


def load_json(name):
    path = DATA / name

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


UKRAINIAN_NAMES = set(load_json("ukrainian_names.json"))
UKRAINIAN_SURNAMES = set(load_json("ukrainian_surnames.json"))
RUSSIAN_NAMES = set(load_json("russian_names.json"))
DIMINUTIVES = set(load_json("diminutives.json"))
BANNED = set(load_json("banned_words.json"))
POLITICIANS = set(load_json("politicians.json"))
BLOGGERS = set(load_json("bloggers.json"))
OBJECTS = set(load_json("objects.json"))
PROJECTS = set(load_json("projects.json"))
ADMINS = set(load_json("admins.json"))
