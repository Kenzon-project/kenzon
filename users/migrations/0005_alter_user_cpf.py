# Generated by Django 4.1.7 on 2023-05-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_cpf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="cpf",
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
