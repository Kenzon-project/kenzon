from rest_framework import serializers
from .models import Produto
from users.serializers import UserSerializer
from categorias.serializer import CategoriaSerializer
from categorias.models import Categoria


class ProdutoSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True)
    user = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="username"
    )

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
            "disponibilidade",
            "user",
            "categorias",
        ]
        extra_kwargs = {"img": {"required": False}}

    def create(self, validated_data):
        categorias = validated_data.pop("categorias")
        produto = Produto.objects.create(**validated_data)

        categorias_list = []
        for c in categorias:
            created = Categoria.objects.get_or_create(**c)
            categorias_list.append(created[0])

        produto.categorias.set(categorias_list)
        return produto

    def update(self, instance, validated_data):
        if validated_data["quantidade_estoque"] == 0:
            validated_data["disponibilidade"] = False
        return super().update(instance, validated_data)

    ...
