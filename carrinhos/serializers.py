from rest_framework import serializers
from .models import Carrinho
from produtos.serializers import ProdutoSerializer


class CarrinhoSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="username"
    )
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = Carrinho
        fields = ["id", "qtd_total", "preco_total", "user", "produtos"]

    def create(self, validated_data):
        return super().create(validated_data)
