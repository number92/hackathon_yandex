import csv
from pprint import pprint

from direction.models import Course, Profession


def create_courses():
    with open("./data/courses.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        accept_obj = []
        for row in csv_reader:
            try:
                proff_objects = []
                prof = [int(obj) for obj in row["professions"].split(",")]
                all_prof = Profession.objects.all()
                for obj in all_prof:
                    if obj.id in prof:
                        proff_objects.append(obj.id)

                course = Course.objects.get_or_create(
                    name=row["name"],
                    link=row["link"],
                    level=row["level"].lower(),
                    duration=row["duration"],
                )

                course[0].save()
                if proff_objects:
                    for i in proff_objects:
                        course[0].professions.add(i)
                accept_obj.append(row["name"])
            except Exception as err:
                pprint(f"ошибка добавления {row['name']}: {err} ")
    pprint(f"Добавлено: {accept_obj}")
