from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSellerOrReadOnly
from .serializers import ProdutoSerializer
from .models import Produto
from users.models import User


class ProdutosView(ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSellerOrReadOnly]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.data.pop("vendedor"))
        serializer.save(vendedor=user)
