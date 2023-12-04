from django.core.management.base import BaseCommand
from .create_direction import create_directions
from .create_profession import create_professions


class Command(BaseCommand):
    """Загрузка данных в БД"""

    def handle(self, *args, **options):
        try:
            create_directions()
            create_professions()
            print("данные загружены.")

        except Exception as er:
            print(er)
