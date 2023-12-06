# Generated by Django 4.2.8 on 2023-12-06 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("direction", "0009_alter_course_professions"),
        ("users", "0005_alter_user_courses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="courses",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to="direction.course",
                verbose_name="Курсы",
            ),
        ),
    ]