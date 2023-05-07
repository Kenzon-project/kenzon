from rest_framework.generics import ListCreateAPIView
from .serializers import CarrinhoSerializer
from .models import CarrinhoProduto
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import UserPermissions
from django.shortcuts import get_object_or_404
from produtos.models import Produto


class CarrinhoView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermissions]

    lookup_field = "id"
    lookup_url_kwarg = "product_id"

    queryset = CarrinhoProduto.objects.all()
    serializer_class = CarrinhoSerializer

    def perform_create(self, serializer):
        self.lookup_field = "product_id"

        carrinho = self.request.user.carrinho
        product = get_object_or_404(Produto, pk=self.kwargs.get("product_id"))

        return serializer.save(carrinho=carrinho, produto=product, quantidade=1)
