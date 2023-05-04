from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from enderecos.models import Endereco


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        address_data = serializer.validated_data.pop("address", None)
        address_obj = Endereco.objects.create(**address_data)

        return serializer.save(address=address_obj)