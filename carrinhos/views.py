from rest_framework.generics import ListCreateAPIView
from rest_framework.views import Response
from .serializers import CarrinhoSerializer
from .models import CarrinhoProduto
from rest_framework_simplejwt.authentication import JWTAuthentication
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

    def perform_create(self, serializer):
        self.lookup_field = "product_id"
        quantidade = self.request.data.get("quantidade", None)
        if quantidade is None:
            quantidade = 1
        carrinho = self.request.user.carrinho
        product = get_object_or_404(Produto, pk=self.kwargs.get("product_id"))
        if product.quantidade_estoque < 1:
            return Response(data="Produto não está disponível", status=400)
        else:
            return serializer.save(
                carrinho=carrinho, produto=product, quantidade=quantidade
            )

    @extend_schema(
        operation_id="carrinho_post",
        request=CarrinhoSerializer,
        description="Rota que adiciona em produto no carrinho",
        tags=["Carrinho"],
        summary="Criação de item para o carrinho",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="carrinho_get",
        description="Rever",
        tags=["Carrinho"],
        summary="Busca todos os carrinhos",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
