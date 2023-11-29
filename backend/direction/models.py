from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Класс пользователей."""

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username", "email"]

    def __str__(self):
        return self.username
