from rest_framework import serializers
from .models import Pedido, Expedicao
from produtos.models import Produto
from django.core.mail import send_mail
from django.conf import settings


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id", "status", "created_at", "updated_at", "produtos", "user_id"]
        read_only_fields = ["id", "created_at", "updated_at", "user_id", "produtos"]
        depth = 1

    def create(self, validated_data: dict) -> Pedido:
        return Pedido.objects.create(**validated_data)

    def update(self, instance: Pedido, validated_data):
        instance.status = validated_data.status
        send_mail(
            subject="ATUALIZAÇÃO DO STATUS DO SEU PEDIDO",
            message=f"O seu pedido agora está {validated_data.status}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.user.email],
            fail_silently=False,
        )
        instance.save()
        return instance


class ExpedicaoSerializer(serializers.ModelSerializer):
    quantidade = serializers.SerializerMethodField()

    def get_quantidade(self, instance: Expedicao):
        produto = Produto.objects.get(id=instance.produto_id)
        novo_estoque = produto.quantidade_estoque - instance.quantidade
        Produto.objects.update({"quantidade_estoque": novo_estoque})

    class Meta:
        model = Expedicao
        fields = ["id", "pedido", "produto", "quantidade"]
        read_only_fields = ["id", "pedido", "produto"]
        extra_kwargs = {"quantidade": {"write_only": True}}
        depth = 1

    def create(self, validated_data: dict) -> Expedicao:
        return Expedicao.objects.create(**validated_data)
