from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


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
    status = models.CharField(
        "Статус",
        choices=settings.STMT_COURSE,
        max_length=256,
        default=None,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="media/images/", blank=True
    )
    duration = models.PositiveIntegerField(
        "Длительность", validators=(MinValueValidator(1),)
    )
    price = models.PositiveIntegerField("Цена", blank=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}, {self.level}"


class Direction(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)
    courses_dir = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курсы направления",
        related_name="courses_dir",
        null=True,
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


class Profession(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)
    short_name = models.CharField("Короткое имя", max_length=256, unique=True)
    direction = models.ManyToManyField(
        Direction,
        through="ProfessionInDirection",
        through_fields=("profession", "direction"),
        related_name="profession",
        verbose_name="Направление",
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="media/images/", blank=True
    )
    description = models.TextField(
        "Описание",
        blank=True,
    )

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.name


class ProfessionInDirection(models.Model):
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        related_name="professions",
        verbose_name="Професии",
    )

    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name="directions",
        verbose_name="Направления",
    )

    class Meta:
        verbose_name = "Профессия в направления"
        verbose_name_plural = "Професии в направлениях"

    def __str__(self):
        return f"{self.direction.name} {self.profession.short_name} "
