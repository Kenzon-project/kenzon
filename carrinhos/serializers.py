from rest_framework import serializers
from .models import CarrinhoProduto
from produtos.serializers import ProdutoSerializer
import ipdb


class CarrinhoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)

    class Meta:
        model = CarrinhoProduto
        fields = ["id", "carrinho_id", "quantidade", "produto"]

    def create(self, validated_data):
        carrinho = validated_data["carrinho"]
        produto = validated_data["produto"]
        quantidade = validated_data["quantidade"]

        carrinho_produto = CarrinhoProduto.objects.filter(
            carrinho=carrinho, produto=produto
        ).first()

        produto.quantidade_estoque -= quantidade
        if produto.quantidade_estoque < 1:
            produto.disponibilidade = False

        produto.save()

        if carrinho_produto:
            carrinho_produto.quantidade += 1
            carrinho_produto.save()
            return carrinho_produto
        else:
            return CarrinhoProduto.objects.create(**validated_data)
