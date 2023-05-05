from django.db import models


class Carrinho(models.Model):
    class Meta:
        ordering = ["id"]

    qtd_total = models.IntegerField()
    preco_total = models.IntegerField()

    user = models.OneToOneField(
        "users.User", related_name="carrinho", on_delete=models.CASCADE
    )
    produtos = models.ManyToManyField(
        "produtos.Produto",
        through="carrinhos.CarrinhoProduto",
        related_name="produto_carrinho",
    )


class CarrinhoProduto(models.Model):
    carrinho_id = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name="carrinho_produto_carrinho"
    )
    produto_id = models.ForeignKey(
        "produtos.Produto",
        on_delete=models.CASCADE,
        related_name="carrinho_produto_produto",
    )
    quantidade = models.IntegerField()
