from django.db import models
from django.contrib.auth.models import AbstractUser
from direction.models import Course


class User(AbstractUser):
    """Класс пользователей."""

    courses = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="courses",
        verbose_name="Курсы",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username", "email"]

    def __str__(self):
        return self.username
