from rest_framework.generics import (ListCreateAPIView, ListAPIView,
                                     UpdateAPIView)
from .serializers import PedidoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Pedido, Expedicao
from produtos.models import Produto
from carrinhos.models import CarrinhoProduto, Carrinho
from .permissions import IsSellerOrAdmin, ListAuth


class PedidoView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ListAuth]

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer: PedidoSerializer):
        serializer.save(user=self.request.user)


class PedidoInfoView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PedidoSerializer

    def get_queryset(self):
        seller = self.request.user.is_seller
        if seller:
            return Pedido.objects.filter(
                produtos__user=self.request.user
            )
        return Pedido.objects.filter(user=self.request.user)


class PedidoUpdateView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
