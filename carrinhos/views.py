from rest_framework.generics import ListCreateAPIView
from .serializers import CarrinhoSerializer
from .models import Carrinho
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import UserPermissions


class CarrinhoView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermissions]

    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    lookup_field = "id"
    lookup_url_kwarg = "user_id"
