def level_b_json():
    value = {
        "junior": "Junior",
        "middle": "Middle",
        "senior": "Senior",
        "lead": "Lead",
    }
    return value


def level_a_json():
    value = {
        "newbie": "Без опыта",
        "junior": "Junior",
        "middle": "Middle",
        "senior": "Senior",
        "lead": "Lead",
    }
    return value


def choosen_level(string: str):
    """Выборка желаемого уровня и уровня ниже"""
    levels = ["junior", "middle", "senior", "lead"]
    if string == levels[0]:
        return string
    if string in levels:
        index = levels.index(string)
        return (levels[index - 1], string)
    return string
