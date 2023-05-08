from rest_framework import serializers
from .models import Carrinho, CarrinhoProduto
from rest_framework.response import Response
from rest_framework import status
from produtos.serializers import ProdutoSerializer
import ipdb


class OnlyCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ["id", "qtd_total", "preco_total"]
        depth = 1


class CarrinhoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    quantidade = serializers.IntegerField(read_only=True)
    carrinho = OnlyCarrinhoSerializer(read_only=True)

    class Meta:
        model = CarrinhoProduto
        fields = ["id", "carrinho_id", "quantidade", "produto", "carrinho"]

    def create(self, validated_data):
        produto = validated_data["produto"]
        quantidade = validated_data["quantidade"]
        valor = produto.valor
        carrinho = validated_data["carrinho"]

        carrinho_produto = CarrinhoProduto.objects.filter(
            carrinho=carrinho, produto=produto
        ).first()
        if not carrinho_produto:
            carrinho.preco_total = valor
            return CarrinhoProduto.objects.create(**validated_data)
