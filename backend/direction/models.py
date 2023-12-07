from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Direction(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)
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
        related_name="directions_professions",
        verbose_name="Направление",
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="images/", blank=True
    )
    description = models.TextField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.name


class ProfessionInDirection(models.Model):
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        related_name="professions_dir",
        verbose_name="Професcии",
    )

    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name="directions_prof",
        verbose_name="Направления",
    )

    class Meta:
        verbose_name = "Профессия в направления"
        verbose_name_plural = "Професcии в направлениях"

    def __str__(self):
        return f"{self.direction.name} {self.profession.short_name} "


class Course(models.Model):
    name = models.CharField("Название", max_length=256)
    level = models.CharField(
        "Уровень",
        choices=settings.DESIRED_LEVEL,
        max_length=256,
        default=None,
    )
    description = models.TextField(
        "Описание",
        blank=True,
    )
    link = models.SlugField("Адрес", blank=True)
    status = models.CharField(
        "Статус",
        choices=settings.STMT_COURSE,
        max_length=256,
        default=None,
        blank=True,
        null=True,
    )
    professions = models.ManyToManyField(
        Profession,
        verbose_name="Профессии курса",
        related_name="course_professions",
        through="CoursesForProfession",
        through_fields=("course", "profession"),
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="images/", blank=True
    )
    duration = models.PositiveIntegerField(
        "Длительность", validators=(MinValueValidator(1),)
    )
    price = models.PositiveIntegerField("Цена", blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}, {self.level}"


class CoursesForProfession(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Курсы",
    )

    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        related_name="professions",
        verbose_name="Профессии",
    )

    class Meta:
        verbose_name = "Курс для профессии"
        verbose_name_plural = "Курсы для профессии"

    def __str__(self):
        return f"{self.id} - курс{self.course} профессия{self.profession}"
