from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from carrinhos.views import CarrinhoView, CarrinhoEdit, CarrinhoListView

urlpatterns = [
    path("users/", views.UserCreate.as_view()),
    path("users/<int:user_id>/", views.UserList.as_view()),
    path("users/perfil/<str:username>/", views.UserPerfil.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/carrinho/<int:product_id>/", CarrinhoView.as_view()),
    path("users/carrinho/", CarrinhoListView.as_view()),
    path("users/carrinho/<int:product_id>/qtd/", CarrinhoEdit.as_view()),
]
