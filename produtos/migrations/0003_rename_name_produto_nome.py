# Generated by Django 4.1.7 on 2023-05-03 19:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("produtos", "0002_rename_user_produto_vendedor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="produto",
            old_name="name",
            new_name="nome",
        ),
    ]