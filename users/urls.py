from django.contrib import admin
from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from carrinhos.views import CarrinhoView

urlpatterns = [
    path("users/", views.UserCreate.as_view()),
    path("users/<int:user_id>", views.UserList.as_view()),
    path("users/perfil/<str:username>", views.UserPerfil.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<int:user_id>/carrinho", CarrinhoView.as_view()),
]
