# Generated by Django 4.2.8 on 2023-12-05 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("direction", "0009_alter_course_professions"),
        ("users", "0002_alter_usergrademap_end_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="courses",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to="direction.course",
                verbose_name="Курсы",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="usergrademap",
            name="end_prof",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="end_prof",
                to="direction.profession",
                verbose_name="Желаемая профессия",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="usergrademap",
            name="start_prof",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="start_prof",
                to="direction.profession",
                verbose_name="Начальная профессия",
            ),
            preserve_default=False,
        ),
    ]
