from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.views import Response, status
from .serializers import PedidoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Pedido
from .permissions import IsSellerOrAdmin, ListAuth, IsSeller
from drf_spectacular.utils import extend_schema


class PedidoView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ListAuth]

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def perform_create(self, serializer: PedidoSerializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="pedido_post",
        description="Rota que cria um pedido",
        tags=["Pedido"],
        summary="Cria um pedido",
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Pedido realizado com sucesso."}, status=status.HTTP_201_CREATED
        )

    @extend_schema(
        operation_id="pedido_get",
        description="Rota que busca todos pedidos do usuário",
        tags=["Pedido"],
        summary="Busca todos os pedido",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PedidoInfoView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSeller]
    serializer_class = PedidoSerializer

    def get_queryset(self):
        return Pedido.objects.filter(produtos__user__id=self.request.user.id)

    @extend_schema(
        operation_id="pedido_get",
        description="Rota que busca todos os pedidos vendidos do usuário",
        tags=["Pedido"],
        summary="Busca todos os pedidos vendidos do usuário",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PedidoInfoViewBuy(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PedidoSerializer

    def get_queryset(self):
        return Pedido.objects.filter(user=self.request.user)

    @extend_schema(
        operation_id="pedido_get",
        description="Rota que busca todos os pedidos comprados do usuário",
        tags=["Pedido"],
        summary="Busca todos os pedidos comprados do usuário",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PedidoUpdateView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdmin]
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

    @extend_schema(
        operation_id="pedido_patch",
        description="Rota que altera o status do pedido",
        tags=["Pedido"],
        summary="Altera status do pedido",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="pedido_put",
        description="Rota que altera o status do pedido",
        tags=["Pedido"],
        summary="Altera status do pedido",
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
