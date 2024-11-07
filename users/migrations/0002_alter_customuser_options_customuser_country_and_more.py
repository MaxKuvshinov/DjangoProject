# Generated by Django 5.1.1 on 2024-10-31 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={"verbose_name": "Пользователь", "verbose_name_plural": "Пользователи"},
        ),
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="users/avatars/"),
        ),
    ]
