from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CarrinhoProduto

@receiver(post_save, sender=CarrinhoProduto)
@receiver(post_delete, sender=CarrinhoProduto)

def atualizar_carrinho_produto(sender, instance, **kwargs):
    carrinho = instance.carrinho
    carrinho.atualizar_carrinho()