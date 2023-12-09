from django.core.management.base import BaseCommand
from .create_direction import create_directions
from .create_profession import create_professions
from .create_courses import create_courses
from .create_users import (
    create_users,
    create_user_course_relation,
    create_user_grade_map,
)


class Command(BaseCommand):
    """Загрузка данных в БД"""

    def handle(self, *args, **options):
        try:
            create_directions()
            create_professions()
            create_courses()
            create_users()
            create_user_course_relation()
            create_user_grade_map()
            print("данные загружены.")

        except Exception as er:
            print(er)
