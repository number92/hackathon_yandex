import csv
from pprint import pprint

from direction.models import Course, Profession


def create_courses():
    with open("./backend/data/courses.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        accept_obj = []
        for row in csv_reader:
            try:
                proff_objects = []
                prof = [int(obj) for obj in row["professions"].split(",")]
                all_prof = Profession.objects.all()
                for obj in all_prof:
                    if obj.id in prof:
                        proff_objects.append(obj)
                one_prof = proff_objects.pop()
                course = Course.objects.create(
                    name=row["name"].lower(),
                    link=row["link"],
                    level=row["level"].lower(),
                    duration=row["duration"],
                    professions=one_prof,
                )

                course.save()
                print(course)
                course.professions.add(proff_objects)
                # course.professions.add(prof)
                print(course.professions)
                # for name in professions:
                #     prof = Profession.objects.get(name=name)
                #     course.professions.add(prof.id)
                # print(course.professions)
                accept_obj.append(row["name"])
            except Exception as err:
                pprint(f"ошибка добавления {row['name']}: {err} ")
    pprint(f"Добавлено: {accept_obj}")
