from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)
from rest_framework.views import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSellerOrReadOnly
from .serializers import ProdutoSerializer
from .models import Produto
from categorias.models import Categoria
from categorias.serializer import CategoriaSerializer
from users.models import User


class ProdutosView(ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSellerOrReadOnly]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        user = User.objects.get(id=1)
        # token
        # serializer.save(vendedor=self.request.user)
        serializer.save(user=user)


class ProdutoDetailsView(RetrieveUpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_url_kwarg = "id"
    lookup_field = "id"


class ProdutoNomeDetailsView(ListAPIView):
    serializer_class = ProdutoSerializer
    lookup_url_kwarg = "nome"
    lookup_field = "nome"

    def get_queryset(self):
        nome = self.kwargs["nome"]
        queryset = Produto.objects.filter(nome__icontains=nome)
        return queryset


class ProdutoCategoriaDetailsView(ListAPIView):
    serializer_class = ProdutoSerializer
    lookup_url_kwarg = "categoria"

    def get_queryset(self):
        categoria: str = self.kwargs["categoria"]
        queryset = Produto.objects.filter(categorias__nome__icontains=categoria)
        return queryset
