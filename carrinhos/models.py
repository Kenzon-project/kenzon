from django.db import models


class Carrinho(models.Model):
    class Meta:
        ordering = ["id"]

    qtd_total = models.IntegerField(null=True, blank=True)
    preco_total = models.IntegerField(null=True, blank=True)

    user = models.OneToOneField(
        "users.User", related_name="carrinho", on_delete=models.CASCADE, blank=True, null=True
    )
    produtos = models.ManyToManyField(
        "produtos.Produto",
        through="carrinhos.CarrinhoProduto",
        related_name="produto_carrinho",
    )

    def atualizar_carrinho(self):
        qtd_total = 0
        preco_total = 0
    
        for item in self.carrinho_produto_carrinhos.all():
            qtd_total += item.quantidade
            preco_total += item.produto.valor * item.quantidade

        self.qtd_total = qtd_total
        self.preco_total = preco_total
        self.save()



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
