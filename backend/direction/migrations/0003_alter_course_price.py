# Generated by Django 4.2.7 on 2023-12-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("direction", "0002_alter_professionindirection_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Цена"
            ),
        ),
    ]
