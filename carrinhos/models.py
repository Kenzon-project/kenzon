from django.db import models


class Carrinho(models.Model):
    class Meta:
        ordering = ["id"]

    qtd_total = models.IntegerField(null=True, blank=True)
    preco_total = models.IntegerField(null=True, blank=True)

    user = models.OneToOneField(
        "users.User", related_name="carrinho", on_delete=models.CASCADE
    )
    produtos = models.ManyToManyField(
        "produtos.Produto",
        through="carrinhos.CarrinhoProduto",
        related_name="produto_carrinho",
    )


class CarrinhoProduto(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name="carrinho_produto_carrinhos"
    )
    produto = models.ForeignKey(
        "produtos.Produto",
        on_delete=models.CASCADE,
        related_name="carrinho_produto_produto",
    )
    quantidade = models.IntegerField(blank=True, default=1)
