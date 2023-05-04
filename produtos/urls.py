from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path("produtos/", views.ProdutosView.as_view()),
    path("produtos/<int:id>/", views.ProdutoIdDetailsView.as_view()),
    path("produtos/<str:nome>/", views.ProdutoNomeDetailsView.as_view()),
    path("produtos/<str:categoria>/", views.ProdutoCategoriaDetailsView.as_view()),
]
