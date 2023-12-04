# import csv
# from pprint import pprint

# from direction.models import Course, Profession


# def create_courses():
#     with open("./data/courses.csv", encoding="utf-8") as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         accept_obj = []
#         for row in csv_reader:
#             try:
#                 Profession.objects.get_or_create(
#                     name=row["name"],
#                     short_name=row["short_name"],
#                     direction=Direction.objects.filter(
#                         name=row["directions"]
#                     ).id,
#                 )
#                 accept_obj.append(row["name"])
#             except Exception as err:
#                 pprint(f"ошибка добавления {row['name']}: {err} ")
#     pprint(f"Добавлено: {accept_obj}")
