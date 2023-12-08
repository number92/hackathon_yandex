from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from direction.models import Profession, Course


class User(AbstractUser):
    """Класс пользователей."""

    email = models.EmailField("email", unique=True)
    courses = models.ManyToManyField(
        Course,
        through="UserCourses",
        through_fields=("user", "course"),
        related_name="usercourses",
        verbose_name="Курсы",
        blank=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "password")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username", "email"]

    def __str__(self):
        return self.username


class UserGradeMap(models.Model):
    user = models.OneToOneField(
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
        "Желаемая квалификация",
        choices=settings.DESIRED_LEVEL,
    )
    start_prof = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        verbose_name="Начальная профессия",
        related_name="start_prof",
        blank=True,
        null=True,
    )
    end_prof = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        verbose_name="Желаемая профессия",
        related_name="end_prof",
    )
    data_joined = models.DateField("Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Карта уровня пользователя"
        verbose_name_plural = "Карта уровней пользователя"

    def __str__(self):
        return (
            f"{self.user.username} - {self.start_level}"
            f"{self.end_prof.name} - {self.end_level}"
        )


class UserCourses(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="user_course",
    )
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE,
        related_name="course_user",
    )
    status = models.CharField(
        "Статус",
        choices=settings.STMT_COURSE,
        max_length=256,
        default=settings.STMT_COURSE[0],
    )

    class Meta:
        verbose_name = "Курс Пользователя"
        verbose_name_plural = "Курсы пользователя"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "course"], name="unique_user_course"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.course}"
