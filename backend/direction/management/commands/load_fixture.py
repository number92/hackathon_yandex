from django.core.management.base import BaseCommand
from .create_direction import create_directions
from .create_profession import create_professions
from .create_courses import create_courses


class Command(BaseCommand):
    """Загрузка данных в БД"""

    def handle(self, *args, **options):
        try:
            # create_directions()
            # create_professions()
            create_courses()
            print("данные загружены.")

        except Exception as er:
            print(er)
