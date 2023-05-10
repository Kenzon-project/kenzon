from django.db import models


class Status(models.TextChoices):
    PEDIDO_REALIZADO = "PEDIDO REALIZADO"
    EM_ANDAMENTO = "EM ANDAMENTO"
    ENTREGUE = "ENTREGUE"


class Pedido(models.Model):
    class Meta:
        ordering = ["id"]

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PEDIDO_REALIZADO
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="pedidos", default=None
    )
    valor_total = models.IntegerField(default=0)
    produtos = models.ManyToManyField(
        "produtos.Produto",
        through="pedidos.Expedicao",
        related_name="pedidos_expedidos",
    )

    def __repr__(self) -> str:
        return f"<Pedido ({self.id}) - {self.status}>"


class Expedicao(models.Model):
    class Meta:
        ordering = ["id"]

    pedido_id = models.ForeignKey(
        "pedidos.Pedido", on_delete=models.CASCADE, related_name="expedicao_pedidos"
    )
    produto_id = models.ForeignKey(
        "produtos.Produto", on_delete=models.CASCADE, related_name="expedicao_produtos"
    )
    quantidade = models.IntegerField()

    def __repr__(self) -> str:
        return f"<Pedido ({self.produto_id.nome}) - {self.pedido_id.status}>"
