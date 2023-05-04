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


class Categoria(models.Model):
    nome = models.CharField(
        max_length=127,
        choices=CategoriasChoices.choices,
        default=CategoriasChoices.DEFAULT,
    )
