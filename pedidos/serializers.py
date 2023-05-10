from rest_framework import serializers
from .models import Pedido, Expedicao
from carrinhos.models import CarrinhoProduto, Carrinho
from django.core.mail import send_mail
from django.conf import settings
from produtos.models import Produto


class PedidoProdutoSerializer(serializers.ModelSerializer):
    quantidade = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = ["id", "nome", "descricao", "img", "valor", "quantidade"]
        depth = 1

    def get_quantidade(self, produto):
        qtd = Expedicao.objects.filter(produto_id=produto).first()
        return qtd.quantidade


class PedidoSerializer(serializers.ModelSerializer):
    produtos = PedidoProdutoSerializer(many=True, read_only=True)
    valor_total_pedido = serializers.SerializerMethodField()
    quantidade = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = [
            "id",
            "status",
            "created_at",
            "updated_at",
            "user_id",
            "valor_total_pedido",
            "quantidade",
            "produtos",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "user_id", "produtos"]

    def get_valor_total_pedido(self, pedido):
        return pedido.valor_total

    def get_quantidade(self, pedido):
        qtd = Expedicao.objects.filter(pedido_id=pedido).first()
        return qtd.quantidade

    def create(self, validated_data: dict):
        user = validated_data["user"]
        carrinho = Carrinho.objects.filter(id=user.carrinho.id).first()
        carrinho_lista = CarrinhoProduto.objects.filter(carrinho=carrinho)
        if not len(carrinho_lista):
            raise serializers.ValidationError(
                {"message": "Seu carrinho não tem produtos para ser criado o pedido."}
            )

        vendedores = []
        produtos = []
        pedidos = []

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
            produto.save()
            produtos.append(produto)
            vendedores.append(produto.user)

        vendedores_set = set(vendedores)

        for vendedor in vendedores_set:
            pedido = Pedido.objects.create(user=validated_data["user"])
            produtos_vendedor = []
            valor_total_pedido = 0

            for produto_list in produtos:
                if produto_list.user == vendedor:
                    produtos_vendedor.append(produto_list)
                    for item in carrinho_lista:
                        if produto_list.id == item.produto.id:
                            valor_total_pedido += (
                                int(produto_list.valor) * item.quantidade
                            )

            for item in carrinho_lista:
                produto = item.produto
                quantidade = item.quantidade
                Expedicao.objects.create(
                    produto_id=produto, pedido_id=pedido, quantidade=quantidade
                )

            pedido.produtos.set(produtos_vendedor)
            pedido.valor_total = carrinho.preco_total
            pedido.valor_total_pedido = valor_total_pedido
            pedido.save()
            send_mail(
                subject=f"PEDIDO {pedido.id} CRIADO COM SUCESSO",
                message=f"Parabéns {user.first_name}, seu pedido foi criado com sucesso.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )
            pedidos.append(pedido)

        carrinho_lista.delete()
        return pedido

    def update(self, instance: Pedido, validated_data: dict):
        if not "status" in validated_data:
            raise serializers.ValidationError(
                {"message": "Nenhum dado para atualizar foi passado"}
            )
        vendedor = Pedido.objects.filter(
            produtos__user=self.context["request"].user, id=instance.id
        )
        if not vendedor:
            raise serializers.ValidationError(
                {"message": "Você não deveria mexer no pedido do coleguinha."}
            )
        instance.status = validated_data["status"]
        send_mail(
            subject=f"ATUALIZAÇÃO DO STATUS DO SEU PEDIDO {instance.id}",
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
