from rest_framework import serializers
from .models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome"]

    def create(self, validated_data):
        return Categoria.objects.get_or_create(**validated_data)
