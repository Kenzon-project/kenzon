from django.urls import path

from . import views

urlpatterns = [
    path("pedidos/", views.PedidoView.as_view()),
    path("pedidos/info/seller/", views.PedidoInfoView.as_view()),
    path("pedidos/info/", views.PedidoInfoViewBuy.as_view()),
    path("pedidos/<int:pk>/", views.PedidoUpdateView.as_view()),
]
