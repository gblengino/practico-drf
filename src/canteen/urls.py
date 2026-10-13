from django.urls import path

from .views import ProductsGenericAPIView, ProductDetailAPIView, ProviderListCreateAPIView

urlpatterns = [
    path("products/", ProductsGenericAPIView.as_view(), name="products_api"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product_detail_api"),
    path("providers/", ProviderListCreateAPIView.as_view(), name="providers_api")
]