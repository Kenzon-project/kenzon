from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
import ipdb
from enderecos.serializers import EnderecoSerializer


class UserSerializer(serializers.ModelSerializer):
    address = EnderecoSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "cpf",
            "birthdate",
            "is_seller",
            "password",
            "is_admin",
            "address",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
            "username": {"read_only": True},
            "is_admin": {"default": False}
        }

    def create(self, validated_data):
        all_users = str(User.objects.count())
        username = validated_data["first_name"] + all_users + "FSDH"

        if validated_data["is_admin"] is True:
            return User.objects.create_superuser(**validated_data, username=username)

        return User.objects.create_user(**validated_data, username=username)
