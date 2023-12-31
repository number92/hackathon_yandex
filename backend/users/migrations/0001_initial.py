# Generated by Django 4.2.8 on 2023-12-09 09:42

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("direction", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ["username", "email"],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserGradeMap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start_level",
                    models.CharField(
                        choices=[
                            ("newbie", "Без опыта"),
                            ("junior", "Junior"),
                            ("middle", "Middle"),
                            ("senior", "Senior"),
                            ("lead", "Lead"),
                        ],
                        verbose_name="Квалификация",
                    ),
                ),
                (
                    "end_level",
                    models.CharField(
                        choices=[
                            ("junior", "Junior"),
                            ("middle", "Middle"),
                            ("senior", "Senior"),
                            ("lead", "Lead"),
                        ],
                        verbose_name="Желаемая квалификация",
                    ),
                ),
                (
                    "data_joined",
                    models.DateField(
                        auto_now_add=True, verbose_name="Дата регистрации"
                    ),
                ),
                (
                    "end_prof",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="end_prof",
                        to="direction.profession",
                        verbose_name="Желаемая профессия",
                    ),
                ),
                (
                    "start_prof",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="start_prof",
                        to="direction.profession",
                        verbose_name="Начальная профессия",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Карта уровня пользователя",
                "verbose_name_plural": "Карта уровней пользователя",
            },
        ),
        migrations.CreateModel(
            name="UserCourses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("not_passed", "Не пройден"),
                            ("in_progress", "В процессе"),
                            ("passed", "Завершен"),
                        ],
                        default=("not_passed", "Не пройден"),
                        max_length=256,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_user",
                        to="direction.course",
                        verbose_name="Курс",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_course",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс Пользователя",
                "verbose_name_plural": "Курсы пользователя",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="courses",
            field=models.ManyToManyField(
                blank=True,
                related_name="usercourses",
                through="users.UserCourses",
                to="direction.course",
                verbose_name="Курсы",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AddConstraint(
            model_name="usercourses",
            constraint=models.UniqueConstraint(
                fields=("user", "course"), name="unique_user_course"
            ),
        ),
    ]
