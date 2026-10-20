from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import GroupEditPermission
from .models import Product, Provider, Order, OrderItem
from .serializers import ProductSerializer, ProductPublicSerializer, ProviderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True).select_related("provider") # Equivalente a un INNER JOIN,
    permission_classes = [IsAuthenticatedOrReadOnly, GroupEditPermission]
    serializer_class = ProductSerializer

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        product = self.get_object()
        product.is_active = False
        product.save()
        return Response({'status':'Product deleted'})

class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Provider.objects.filter(is_active=True)
    serializer_class = ProviderSerializer

