from django.urls import path

from . import views

urlpatterns = [
    path("pedidos/", views.PedidoView.as_view()),
    path("pedidos/info/", views.PedidoInfoView.as_view()),
    path("pedidos/<int:pk>/", views.PedidoUpdateView.as_view()),
]
