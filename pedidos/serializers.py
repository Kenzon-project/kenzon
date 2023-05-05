from rest_framework import serializers
from .models import Pedido, Expedicao


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id", "status", "created_at", "updated_at", "produtos", "user"]
        read_only_fields = ["id", "created_at", "updated_at", "user", "produtos"]
        depth = 1

    def create(self, validated_data: dict) -> Pedido:
        return Pedido.objects.create(**validated_data)


class ExpedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedicao
        fields = ["id", "pedido", "produto", "quantidade"]
        read_only_fields = ["id", "pedido", "produto"]
        extra_kwargs = {"quantidade": {"write_only": True}}
        depth = 1

    def create(self, validated_data: dict) -> Expedicao:
        return Expedicao.objects.create(**validated_data)
