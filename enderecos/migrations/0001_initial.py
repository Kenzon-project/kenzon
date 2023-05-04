# Generated by Django 4.1.7 on 2023-05-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Endereco",
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
                ("bairro", models.CharField(max_length=50)),
                ("rua", models.CharField(max_length=50)),
                ("numero", models.CharField(max_length=10)),
                ("cidade", models.CharField(max_length=50)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("AC", "Acre Ac"),
                            ("AL", "Alagoas Al"),
                            ("AP", "Amapa Ap"),
                            ("AM", "Amazonas Am"),
                            ("BA", "Bahia Ba"),
                            ("CE", "Ceara Ce"),
                            ("DF", "Distrito Federal Df"),
                            ("ES", "Espirito Santo Es"),
                            ("GO", "Goias Go"),
                            ("MA", "Maranhao Ma"),
                            ("MT", "Mato Grosso Mt"),
                            ("MS", "Mato Grosso Do Sul Ms"),
                            ("MG", "Minas Gerais Mg"),
                            ("PA", "Para Pa"),
                            ("PB", "Paraiba Pb"),
                            ("PR", "Parana Pr"),
                            ("PE", "Pernambuco Pe"),
                            ("PI", "Piaui Pi"),
                            ("RJ", "Rio De Janeiro Rj"),
                            ("RN", "Rio Grande Do Norte Rn"),
                            ("RS", "Rio Grande Do Sul Rs"),
                            ("RO", "Rondonia Ro"),
                            ("RR", "Roraima Rr"),
                            ("SC", "Santa Catarina Sc"),
                            ("SP", "Sao Paulo Sp"),
                            ("SE", "Sergipe Se"),
                            ("TO", "Tocantins To"),
                        ],
                        max_length=2,
                    ),
                ),
                ("cep", models.IntegerField()),
                ("complemento", models.CharField(max_length=50)),
            ],
        ),
    ]
