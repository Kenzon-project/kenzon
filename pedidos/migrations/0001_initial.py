# Generated by Django 4.1.7 on 2023-05-05 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("produtos", "0003_alter_produto_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Expedicao",
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
                ("quantidade", models.IntegerField()),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Pedido",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PEDIDO REALIZADO", "Pedido Realizado"),
                            ("EM ANDAMENTO", "Em Andamento"),
                            ("ENTREGUE", "Entregue"),
                        ],
                        default="PEDIDO REALIZADO",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "produtos",
                    models.ManyToManyField(
                        related_name="pedidos_expedidos",
                        through="pedidos.Expedicao",
                        to="produtos.produto",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pedidos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="expedicao",
            name="pedido_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="expedicao_pedidos",
                to="pedidos.pedido",
            ),
        ),
        migrations.AddField(
            model_name="expedicao",
            name="produto_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="expedicao_produtos",
                to="produtos.produto",
            ),
        ),
    ]
