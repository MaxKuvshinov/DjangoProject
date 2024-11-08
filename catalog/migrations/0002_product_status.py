# Generated by Django 5.1.3 on 2024-11-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[("awaiting_publication", "Ждет публикации"), ("publication", "Опубликовано")],
                default="awaiting_publication",
                max_length=20,
                verbose_name="Статус публикации",
            ),
        ),
    ]