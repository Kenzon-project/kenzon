from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from enderecos.serializers import EnderecoSerializer
from enderecos.models import Endereco
from produtos.serializers import ProdutoSerializer


class UserSerializer(serializers.ModelSerializer):
    address = EnderecoSerializer()
    produtos = ProdutoSerializer(many=True, read_only=True)

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
            "produtos",
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

        return create_user

    def update(self, instance, validated_data):
        is_admin = validated_data.keys()
        address_data = validated_data.pop("address", None)
        if "is_admin" in is_admin:
            validated_data.pop("is_admin")

        instance.__dict__.update(**validated_data)
        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        if address_data:
            Endereco.objects.update(**address_data)

        instance.save()
        return instance


class PerfilSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = User
        fields = ["username", "email", "is_seller", "address", "produtos"]

    def get_address(self, obj):
        endereco = obj.address
        return [{"cidade": endereco.cidade, "estado": endereco.estado}]
