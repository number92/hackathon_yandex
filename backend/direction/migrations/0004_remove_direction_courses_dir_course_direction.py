# Generated by Django 4.2.7 on 2023-12-02 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("direction", "0003_alter_course_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="direction",
            name="courses_dir",
        ),
        migrations.AddField(
            model_name="course",
            name="direction",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="direction",
                to="direction.direction",
                verbose_name="Курсы направления",
            ),
        ),
    ]
