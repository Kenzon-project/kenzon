from django.db import models


class CategoriasChoices(models.TextChoices):
    INFORMATICA = "Informática"
    ELETRODOMESTICOS = "Eletrodomésticos"
    CASA = "Casa"
    LIVROS = "Livros"
    ELETRONICOS = "Eletrônicos"
    GAMES = "Games"
    BRINQUEDOS = "Brinquedos"
    CRIANCAS = "Crianças"
    DEFAULT = "Not Informed"


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=255)
    img = models.URLField(
        max_length=255,
        default="https://as1.ftcdn.net/v2/jpg/05/04/28/96/1000_F_504289605_zehJiK0tCuZLP2MdfFBpcJdOVxKLnXg1.jpg",
    )
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    quantidade_estoque = models.IntegerField()
    vendidos = models.IntegerField(default=0)
    vendedor = models.ForeignKey(
        "users.User",
        related_name="produtos",
        on_delete=models.RESTRICT,
    )
    categorias = models.CharField(
        max_length=127,
        choices=CategoriasChoices.choices,
        default=CategoriasChoices.DEFAULT,
    )
