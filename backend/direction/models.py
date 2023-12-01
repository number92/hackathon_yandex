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
    image = models.ImageField(
        verbose_name="Изображение", upload_to="media/images/", blank=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)
    courses_dir = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курсы направления",
        related_name="courses_dir",
    )
    link = models.SlugField("Ссылка", unique=True, blank=True)
    description = models.TextField(
        "Описание",
        blank=True,
    )

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    def __str__(self):
        return self.name
