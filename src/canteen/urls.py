from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProviderViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')
router.register(r'providers', ProviderViewSet, basename='provider')

urlpatterns = [
    path("", include(router.urls)),
]