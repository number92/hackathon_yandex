from direction.models import Direction
from pprint import pprint


DIRECTIONS = ("Аналитика", "Менеджмент", "Дизайн")


def create_directions():
    accept_obj = []

    for obj in DIRECTIONS:
        try:
            Direction.objects.get_or_create(name=obj)
            accept_obj.append(obj)
        except Exception as err:
            pprint(f"ошибка добавления {obj}: {err} ")
    pprint(f"Добавлено: {accept_obj}")
