from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from enderecos.serializers import EnderecoSerializer
from carrinhos.models import Carrinho


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
            "carrinho",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
            "username": {"read_only": True},
            "carrinho": {"read_only": True},
            "is_admin": {"default": False},
        }

    def create(self, validated_data):
        all_users = str(User.objects.count())
        username = validated_data["first_name"] + all_users + "FSDH"

        if validated_data["is_admin"] is True:
            return User.objects.create_superuser(**validated_data, username=username)

        create_user = User.objects.create_user(**validated_data, username=username)
        Carrinho.objects.create(user=create_user)

        return create_user

    def update(self, instance, validated_data):
        is_admin = validated_data.keys()
        if "is_admin" in is_admin:
            validated_data.pop("is_admin")
        instance.__dict__.update(**validated_data)
        instance.set_password(instance.password)
        instance.save()
        return instance


class PerfilSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "is_seller",
            "address",
        ]

    def get_address(self, obj):
        endereco = obj.address
        return [{"cidade": endereco.cidade, "estado": endereco.estado}]
