from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    cpf = models.PositiveBigIntegerField(
        unique=True, validators=[MaxValueValidator(99999999999)]
    )
    birthdate = models.DateField()
    is_seller = models.BooleanField(blank=True, default=False)
    is_admin = models.BooleanField(default=False)

    address = models.OneToOneField(
        "enderecos.Endereco", 
        on_delete=models.CASCADE,
        related_name="user_endereco",
    )
