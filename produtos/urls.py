from . import views
from django.urls import path


urlpatterns = [
    path("produtos/", views.ProdutosView.as_view()),
    path("produtos/<int:produto_id>/", views.ProdutoDetailsView.as_view()),
]
