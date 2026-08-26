from django.urls import path

from .views import products, product_detail

urlpatterns = [
    path("", products, name="products_api"),
    path("<int:pk>/", product_detail, name="product_detail_api")
]