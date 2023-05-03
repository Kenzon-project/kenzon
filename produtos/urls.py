from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path("produtos/", views.ProdutosView.as_view()),
    # path("produtos/<int:id>/"),
    # path("produtos/<char:nome>/"),
    # path("produtos/<char:categoria>/"),
]
