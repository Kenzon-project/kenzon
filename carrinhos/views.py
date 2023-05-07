from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import CarrinhoSerializer
from .models import CarrinhoProduto
from carrinhos.models import Carrinho
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import UserPermissions
from django.shortcuts import get_object_or_404
from produtos.models import Produto
from drf_spectacular.utils import extend_schema


class CarrinhoView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermissions]

    lookup_field = "id"
    lookup_url_kwarg = "product_id"

    queryset = CarrinhoProduto.objects.all()
    serializer_class = CarrinhoSerializer

    def create(self, request, *args, **kwargs):
        product = get_object_or_404(Produto, pk=self.kwargs.get("product_id"))
        if not product.quantidade_estoque:
            return Response(
                {"message": "Produto sem estoque."}, status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        product = get_object_or_404(Produto, pk=self.kwargs.get("product_id"))
        quantidade = 1
        carrinho = self.request.user.carrinho

        return serializer.save(
            carrinho=carrinho, produto=product, quantidade=quantidade
        )


class CarrinhoEdit(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CarrinhoProduto.objects.all()
    serializer_class = CarrinhoSerializer

    lookup_field = "produto_id"
    lookup_url_kwarg = "product_id"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {
            self.lookup_field: self.kwargs[self.lookup_url_kwarg],
            "carrinho": self.request.user.carrinho,
        }
        obj = get_object_or_404(queryset, **filter_kwargs)

        return obj

    def update(self, request, *args, **kwargs):
        carrinho_produto = (
            self.get_queryset()
            .filter(
                produto_id=self.kwargs["product_id"],
                carrinho=self.request.user.carrinho,
            )
            .first()
        )
        if not carrinho_produto:
            return Response({"Message": "Produto não encontrado no carrinho"}, 404)

        produto = carrinho_produto.produto
        carrinho = carrinho_produto.carrinho

        if not carrinho_produto:
            return Response({"Message": "Produto não encontrado no carrinho"}, 404)

        url_param = self.request.query_params

        if not produto.quantidade_estoque:
            carrinho_produto.delete()
            return Response({"Message": "Esse produto não está mais disponível"}, 404)

        if "add" in url_param:
            if carrinho_produto.quantidade >= produto.quantidade_estoque:
                return Response({"Message": "Quantidade máxima atingida"}, 404)
            carrinho_produto.quantidade += 1

        elif "remove" in url_param:
            if carrinho_produto.quantidade == 1:
                carrinho_produto.delete()
                return Response({"Message": "Produto removido com sucesso"}, 404)
            carrinho_produto.quantidade -= 1

        carrinho_produto.save()

        return super().update(request, *args, **kwargs)
