from django.shortcuts import render
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, PerfilSerializer
from .permissions import UserPermissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from enderecos.models import Endereco
import ipdb


class UserCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_authenticators(self):
        if self.request.method == 'GET':
            return [JWTAuthentication()]
        return []
    

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminUser()]
        return []


    def perform_create(self, serializer):
        address_data = serializer.validated_data.pop("address", None)
        address_obj = Endereco.objects.create(**address_data)

        return serializer.save(address=address_obj)

class UserList(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserPermissions]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = "id"
    lookup_url_kwarg = "user_id"

class UserPerfil(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = PerfilSerializer

    lookup_field = "username"
    lookup_url_kwarg = "username"