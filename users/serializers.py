from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
import ipdb


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "cpf", "birthdate", "is_seller", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())]
            }
        }
    def create(self, validated_data):
        all_users = str(User.objects.count())
        username = validated_data["first_name"] + all_users + "FSDH"
        return User.objects.create_user(**validated_data, username=username)
    