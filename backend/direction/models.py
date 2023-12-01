from django.db import models
from django.conf import settings


class Course(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)
    level = models.CharField(
        "Уровень",
        choices=settings.LEVEL,
        max_length=256,
        default=None,
    )
    description = models.TextField(
        "Описание",
        blank=True,
    )
    link = models.SlugField("Адрес", unique=True, blank=False)
    progress = models.CharField(
        "Прогресс",
        choices=settings.STMT_COURSE,
        max_length=256,
        default=None,
        blank=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name
