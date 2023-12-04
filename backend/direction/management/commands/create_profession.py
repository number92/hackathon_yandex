import csv
from pprint import pprint

from direction.models import Direction, Profession, ProfessionInDirection


def create_professions():
    with open("./data/professions.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        accept_obj = []
        for row in csv_reader:
            try:
                dir = Direction.objects.get(name=row["directions"])
                obj = Profession.objects.get_or_create(
                    name=row["name"],
                    short_name=row["short_name"],
                )
                obj[0].save()
                obj[0].direction.add(dir.id)
                accept_obj.append(row["name"])
                prof = Profession.objects.get(name=row["name"])

                ProfessionInDirection.objects.get_or_create(
                    profession=prof.id, direction=dir.id
                )
                pprint(f"связь {row['name']} - {row['directions']} создана")
            except Exception as err:
                pprint(f"ошибка добавления {row['name']}: {err} ")
    pprint(f"Добавлено: {accept_obj}")
