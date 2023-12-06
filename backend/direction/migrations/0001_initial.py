# Generated by Django 4.2.8 on 2023-12-06 17:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Direction",
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
                    "name",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Направление",
                "verbose_name_plural": "Направления",
            },
        ),
        migrations.CreateModel(
            name="Profession",
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
                    "name",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        max_length=256,
                        unique=True,
                        verbose_name="Короткое имя",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="images/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Профессия",
                "verbose_name_plural": "Профессии",
            },
        ),
        migrations.CreateModel(
            name="ProfessionInDirection",
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
                    "direction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="directions",
                        to="direction.direction",
                        verbose_name="Направления",
                    ),
                ),
                (
                    "profession",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professions",
                        to="direction.profession",
                        verbose_name="Професcии",
                    ),
                ),
            ],
            options={
                "verbose_name": "Профессия в направления",
                "verbose_name_plural": "Професcии в направлениях",
            },
        ),
        migrations.AddField(
            model_name="profession",
            name="direction",
            field=models.ManyToManyField(
                related_name="profession",
                through="direction.ProfessionInDirection",
                to="direction.direction",
                verbose_name="Направление",
            ),
        ),
        migrations.CreateModel(
            name="Course",
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
                    "name",
                    models.CharField(max_length=256, verbose_name="Название"),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("junior", "Junior"),
                            ("middle", "Middle"),
                            ("senior", "Senior"),
                            ("lead", "Lead"),
                        ],
                        default=None,
                        max_length=256,
                        verbose_name="Уровень",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Описание"),
                ),
                ("link", models.SlugField(blank=True, verbose_name="Адрес")),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("passed", "Завершен"),
                            ("not_passed", "Не пройден"),
                            ("in_progress", "В процессе"),
                        ],
                        default=None,
                        max_length=256,
                        null=True,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="images/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1)
                        ],
                        verbose_name="Длительность",
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Цена"
                    ),
                ),
                (
                    "professions",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profession",
                        to="direction.profession",
                        verbose_name="Профессии курса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
    ]
