from rest_framework import serializers
from .models import Carrinho, CarrinhoProduto
from produtos.serializers import ProdutoSerializer


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
        user = self.context["request"].user
        produto = validated_data["produto"]
        carrinho = validated_data["carrinho"]

        carrinho_produto = CarrinhoProduto.objects.filter(
            carrinho=carrinho, produto=produto
        ).first()
        if carrinho_produto:
            if produto.id == carrinho_produto.produto.id:
                raise serializers.ValidationError(
                    {"message": "Produto já adicionado ao carrinho."}
                )
        quantidade = validated_data["quantidade"]
        if user.is_seller:
            if produto.user == user:
                raise serializers.ValidationError(
                    {"message": "Não é possível comprar o próprio produto."},
                )
        valor = produto.valor

        if not carrinho_produto:
            carrinho.preco_total = valor
            return CarrinhoProduto.objects.create(**validated_data)
