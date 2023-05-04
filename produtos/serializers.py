from rest_framework import serializers
from .models import Produto
from users.serializers import UserSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    # vendedor = UserSerializer()

    class Meta:
        model = Produto
        fields = [
            "id",
            "nome",
            "descricao",
            "img",
            "valor",
            "quantidade_estoque",
            "vendidos",
            "vendedor",
            "categorias",
        ]

    def create(self, validated_data):
        return Produto.objects.create(**validated_data)

    ...
