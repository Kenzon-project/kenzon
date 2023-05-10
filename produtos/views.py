from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSellerOrReadOnly, IsSellerOwnerOrReadOnly
from .serializers import ProdutoSerializer
from .models import Produto
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class ProdutosView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrReadOnly]

    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Produto.objects.all()
        categoria_name = self.request.query_params.get("categoria", None)
        nome = self.request.query_params.get("nome", None)
        if nome is not None:
            queryset = Produto.objects.filter(nome__icontains=nome)
            for produto in queryset:
                if produto.quantidade_estoque < 1:
                    produto.disponibilidade = False

        if categoria_name is not None:
            queryset = Produto.objects.filter(
                categorias__nome__icontains=categoria_name
            )
            for produto in queryset:
                if produto.quantidade_estoque < 1:
                    produto.disponibilidade = False
                    produto.save()
        return queryset

    @extend_schema(
        operation_id="produto_post",
        description="Rota de criação de produto",
        tags=["Produto"],
        summary="Criar produto",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        operation_id="produto_get",
        description="Buscar produto, esta rota não precisa de autenticação",
        parameters=[
            OpenApiParameter(
                "page",
                OpenApiTypes.INT,
                OpenApiParameter.QUERY,
                description="Número da página",
            ),
            OpenApiParameter(
                "nome",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="Filtro por nome do produto",
            ),
            OpenApiParameter(
                "categoria",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="Filtro por nome da categoria",
            ),
        ],
        responses=ProdutoSerializer,
        tags=["Produto"],
        summary="Rota que busca todos os de produto ",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProdutoDetailsView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerOrReadOnly]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_url_kwarg = "produto_id"
    lookup_field = "id"

    @extend_schema(
        operation_id="produto_get",
        description="Rota de busca de produto pelo id",
        tags=["Produto"],
        summary="Buscar produto pelo id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="produto_patch",
        request=ProdutoSerializer,
        description="Rota de alteração de dados de produto",
        tags=["Produto"],
        summary="Altera dados de um produto",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="produto_put",
        description="Rota de alteração TODOS os de dados de produto",
        tags=["Produto"],
        summary="Altera TODOS dados de um produto ",
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="produto_delete",
        description="Rota de deleção de produto",
        tags=["Produto"],
        summary="Deleta um produto",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
