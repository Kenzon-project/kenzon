from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, PerfilSerializer
from .permissions import UserPermissions, UserPermissionCreate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from enderecos.models import Endereco
from drf_spectacular.utils import extend_schema


class UserCreate(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermissionCreate]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        address_data = serializer.validated_data.pop("address", None)
        address_obj = Endereco.objects.create(**address_data)

        return serializer.save(address=address_obj)

    @extend_schema(
        operation_id="user_post",
        request=UserSerializer,
        responses={
            201: UserSerializer,
        },
        description="Rota de criação de usuário",
        tags=["Usuário"],
        summary="Criação de usuário",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_get",
        description="Rota que busca todos os usuários cadastrados",
        tags=["Usuário"],
        summary="Busca todos os usuários",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserList(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermissions]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = "id"
    lookup_url_kwarg = "user_id"

    @extend_schema(
        operation_id="user_get",
        description="Rota de busca de usuário pelo id",
        tags=["Usuário"],
        summary="Buscar usuário pelo id",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_patch",
        description="Rota de alteração de dados de usuário",
        tags=["Usuário"],
        summary="Altera dados de um usuário",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_put",
        description="Rota de alteração TODOS os de dados de usuário",
        tags=["Usuário"],
        summary="Altera TODOS dados de um usuário ",
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_delete",
        description="Rota de deleção de usuário",
        tags=["Usuário"],
        summary="Deleta um usuário",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UserPerfil(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = PerfilSerializer

    lookup_field = "username"
    lookup_url_kwarg = "username"

    @extend_schema(
        operation_id="user_get",
        description="Rota de busca de usuário pelo username",
        tags=["Usuário"],
        summary="Buscar usuário pelo usename",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
