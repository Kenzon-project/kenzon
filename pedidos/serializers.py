from rest_framework import serializers
from .models import Pedido, Expedicao
from produtos.models import Produto
from produtos.serializers import ProdutoSerializerGet
from carrinhos.models import CarrinhoProduto, Carrinho
from django.core.mail import send_mail
from django.conf import settings


class PedidoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializerGet(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = [
            "id", "status", "created_at", "updated_at", "produtos", "user_id"]
        read_only_fields = [
            "id", "created_at", "updated_at", "user_id", "produtos"]
        depth = 1

    def create(self, validated_data: dict) -> Pedido:
        pedido = Pedido.objects.create(user=validated_data["user"])
        carrinho = Carrinho.objects.filter(
            id=validated_data["user"].carrinho.id).first()
        carrinho_lista = CarrinhoProduto.objects.filter(
            carrinho=carrinho)
        produtos = []
        for item in carrinho_lista:
            produto = item.produto
            produtos.append(produto)

        for item in carrinho_lista:
            produto = item.produto
            quantidade = item.quantidade
            Expedicao.objects.create(
                produto_id=produto, pedido_id=pedido, quantidade=quantidade)
        pedido.produtos.set(produtos)
        return pedido

    def update(self, instance: Pedido, validated_data: dict):
        instance.status = validated_data["status"]
        print(instance.status)
        send_mail(
            subject="ATUALIZAÇÃO DO STATUS DO SEU PEDIDO",
            message=f"O seu pedido agora está {instance.status}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.user.email],
            fail_silently=False,
        )
        instance.save()
        return instance


class ExpedicaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expedicao
        fields = ["id", "pedido", "produto", "quantidade"]
        read_only_fields = ["id", "pedido", "produto"]
        extra_kwargs = {"quantidade": {"write_only": True}}
        depth = 1

    def create(self, validated_data: dict) -> Expedicao:
        return Expedicao.objects.create(**validated_data)
