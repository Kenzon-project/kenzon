from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSellerOrReadOnly, IsSellerOwnerOrReadOnly
from .serializers import ProdutoSerializer
from .models import Produto
import ipdb


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
                if produto.quantidade_estoque == 0:
                    produto.disponibilidade = False

        if categoria_name is not None:
            queryset = Produto.objects.filter(
                categorias__nome__icontains=categoria_name
            )
            for produto in queryset:
                if produto.quantidade_estoque == 0:
                    produto.disponibilidade = False
        return queryset


class ProdutoDetailsView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerOrReadOnly]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_url_kwarg = "produto_id"
    lookup_field = "id"
