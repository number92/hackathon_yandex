from direction.models import Course


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
        return [levels[index - 1], string]
    return string


def calculating_percent(obj):
    user_courses = 0
    all_courses = 0
    level_range = choosen_level(obj.end_level)
    for i in level_range:
        all_courses += Course.objects.filter(
            level=i, professions=obj.end_prof
        ).count()
        all_user_course = obj.user.courses.filter(
            level=i, professions=obj.end_prof
        )
        for k in all_user_course:
            count_in_progress = k.course_user.filter(
                status="in_progress"
            ).count()
            if count_in_progress > 0:
                user_courses += 0.5
            count_passed = k.course_user.filter(status="passed").count()
            if count_passed > 0:
                user_courses += 1
    if user_courses != 0 and all_courses != 0:
        status_in_perscent = (user_courses / all_courses) * 100
        return f"{int(status_in_perscent)}%"
    return "0%"
