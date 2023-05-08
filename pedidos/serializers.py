from rest_framework import serializers
from .models import Pedido, Expedicao
from carrinhos.models import CarrinhoProduto, Carrinho
from django.core.mail import send_mail
from django.conf import settings
from produtos.models import Produto
import ipdb

class PedidoProdutoSerializer(serializers.ModelSerializer):
    quantidade = serializers.SerializerMethodField()
    valor_total = serializers.SerializerMethodField()


    class Meta:
        model = Produto
        fields = [
            "id",
            "nome",
            "descricao",
            "img",
            "valor",
            "valor_total",
            "quantidade",
        ]
            "id", "nome", "descricao", "img", "valor", "valor_total", "quantidade"]
        depth = 1

    def get_quantidade(self, produto):
        if self.context["request"].method == "POST":
            user = self.context["request"].user
            carrinho_produto = CarrinhoProduto.objects.filter(
                carrinho=user.carrinho.id, produto=produto
            ).first()
        else:
            carrinho_produto = Expedicao.objects.filter(produto_id=produto).first()

        return carrinho_produto.quantidade if carrinho_produto else 0

    def get_valor_total(self, produto):
        if self.context["request"].method == "POST":
            user = self.context["request"].user
            carrinho_produto = CarrinhoProduto.objects.filter(
                carrinho=user.carrinho.id, produto=produto
            ).first()
            valor_total = carrinho_produto.quantidade * produto.valor
        else:
            carrinho_produto = carrinho_produto = Expedicao.objects.filter(
                produto_id=produto
            ).first()
            valor_total = carrinho_produto.quantidade * produto.valor

        return valor_total if carrinho_produto else 0

  
    def to_representation(self, instance):
        data = super().to_representation(instance)

        user = self.context["request"].user
        carrinho_produto = CarrinhoProduto.objects.filter(
            carrinho=user.carrinho.id, produto=instance.id
        ).first()
        if carrinho_produto:
            if self.context["request"].method == "POST":
                carrinho_produto.delete()
        return data


class PedidoSerializer(serializers.ModelSerializer):
    produtos = PedidoProdutoSerializer(many=True, read_only=True)
    valor_total_pedido = serializers.IntegerField(required=False)

    class Meta:
        model = Pedido
        fields = [
            "id",
            "status",
            "created_at",
            "updated_at",
            "produtos",
            "user_id",
            "valor_total_pedido",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "user_id", "produtos"]
        depth = 1

    def create(self, validated_data: dict) -> Pedido:
        pedido = Pedido.objects.create(user=validated_data["user"])
        carrinho = Carrinho.objects.filter(
            id=validated_data["user"].carrinho.id
        ).first()
        carrinho_lista = CarrinhoProduto.objects.filter(carrinho=carrinho)
        if not len(carrinho_lista):
            raise serializers.ValidationError(
                {"message": "Seu carrinho não tem produtos para ser criado o pedido."}
            )
        produtos = []
        valor_total_pedido = 0
        for item in carrinho_lista:
            if item.quantidade > item.produto.quantidade_estoque:
                carrinho_lista.delete()
                raise serializers.ValidationError(
                    {
                        "message": "Ooops, parece que o estoque acabou, atualize seu carrinho novamente"
                    }
                )
            produto = item.produto
            produto.vendidos += item.quantidade
            produto.quantidade_estoque -= item.quantidade
            valor_total_pedido += produto.valor * item.quantidade
            produto.save()

            produtos.append(produto)

        for item in carrinho_lista:
            produto = item.produto
            quantidade = item.quantidade
            Expedicao.objects.create(
                produto_id=produto, pedido_id=pedido, quantidade=quantidade)

        pedido.produtos.set(produtos)
        pedido.valor_total = carrinho.preco_total
        pedido.valor_total_pedido = valor_total_pedido
        pedido.save()
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
