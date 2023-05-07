from django.db import models


class Produto(models.Model):
    class Meta:
        ordering = ["id"]

    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    img = models.URLField(
        max_length=255,
        default="https://as1.ftcdn.net/v2/jpg/05/04/28/96/1000_F_504289605_zehJiK0tCuZLP2MdfFBpcJdOVxKLnXg1.jpg",
    )
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    quantidade_estoque = models.IntegerField()
    disponibilidade = models.BooleanField(default=True)
    vendidos = models.IntegerField(default=0)
    user = models.ForeignKey(
        "users.User",
        related_name="produtos",
        on_delete=models.RESTRICT,
    )
    categorias = models.ManyToManyField("categorias.Categoria", related_name="produtos_cat")
