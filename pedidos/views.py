from rest_framework.generics import ListCreateAPIView
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PedidoView(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
