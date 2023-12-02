from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from direction.models import Course, Profession


class User(AbstractUser):
    """Класс пользователей."""

    email = models.EmailField(("email"))
    courses = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        related_name="courses",
        verbose_name="Курсы",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username", "email"]

    def __str__(self):
        return self.username


class UserGradeMap(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Пользователь",
    )
    start_level = models.CharField(
        "Квалификация",
        choices=settings.LEVEL,
    )
    end_level = models.CharField(
        "Квалификация",
        choices=settings.LEVEL,
    )
    start_prof = models.ForeignKey(
        Profession,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Начальная профессия",
        related_name="start_prof",
    )
    end_prof = models.ForeignKey(
        Profession,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Желаемая профессия",
        related_name="end_prof",
    )
    data_joined = models.DateField("Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Карта уровня пользователя"
        verbose_name_plural = "Карта уровней пользователя"

    def __str__(self):
        return (
            f"{self.start_prof.name} - {self.start_level}\n"
            f"{self.end_prof.name} - {self.end_level}"
        )
