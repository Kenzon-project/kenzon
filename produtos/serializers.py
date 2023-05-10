from rest_framework import serializers
from .models import Produto
from categorias.serializer import CategoriaSerializer
from categorias.models import Categoria
from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Exemplo de criação de produto ",
            summary="Criação de produtos",
            description="Rota para criação de produtos",
            value={
                "nome": "Mesa de Escritório",
                "descricao": "Mesa de Escritório em L Estilo Industrial 1,50mX1,50m Kuadra, Trevalla, Preto Ônix/Est.Preta",
                "valor": 399.94,
                "quantidade_estoque": 2,
                "img": "https://m.media-amazon.com/images/I/71vJtkqhn+L._AC_SY300_SX300_.jpg",
                "categorias": [{"nome": "Casa"}],
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Exemplo de alteração de produto PATCH",
            summary="Alretação de produtos",
            description="Rota PATCH para alteração de produtos",
            value={
                "nome": "Mesa de Escritório 2",
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Exemplo de alteração de produto PUT",
            summary="Alretação de produtos ",
            description="Rota PUT para alteração de produtos",
            value={
                "nome": "Mesa de Escritório",
                "descricao": "Mesa de Escritório em L Estilo Industrial 1,50mX1,50m Kuadra, Trevalla, Preto Ônix/Est.Preta",
                "valor": 399.94,
                "quantidade_estoque": 2,
                "img": "https://m.media-amazon.com/images/I/71vJtkqhn+L._AC_SY300_SX300_.jpg",
                "categorias": [{"nome": "Casa"}],
            },
            request_only=True,
            response_only=False,
        ),
    ],
)
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
            "vendidos",
            "quantidade_estoque",
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


class ProdutoSerializerGet(serializers.ModelSerializer):
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
            "vendidos",
            "disponibilidade",
            "user",
            "categorias",
        ]
        extra_kwargs = {"img": {"required": False}}
