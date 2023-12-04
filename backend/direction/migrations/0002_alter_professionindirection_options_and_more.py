# Generated by Django 4.2.7 on 2023-12-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("direction", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="professionindirection",
            options={
                "verbose_name": "Профессия в направления",
                "verbose_name_plural": "Професии в направлениях",
            },
        ),
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.IntegerField(blank=True, verbose_name="Цена"),
        ),
    ]