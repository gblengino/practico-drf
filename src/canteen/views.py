from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Provider, Order, OrderItem
from .serializers import ProductSerializer, ProductPublicSerializer, ProviderSerializer

# Clase Generic APIView
# Django utiliza una semantica propia para los metodos
# List => Get all
# Create => Post
# Retrieve => Get by ID
# Update => Put
# Destroy => Delete

class ProductsGenericAPIView(APIView):
    def get(self, request):
        products = Product.objects.all().select_related("provider") # Equivalente a un INNER JOIN,
        products_serialized = ProductPublicSerializer(products, many=True)
        return Response(products_serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        new_product_serialized = ProductSerializer(data=request.data)
        if new_product_serialized.is_valid():
            new_product_serialized.save()
            return Response({"message":"Product created"},status=status.HTTP_201_CREATED)
        return Response(
            {"message":"Invalid data"},status=status.HTTP_400_BAD_REQUEST,)

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().select_related("provider")
    serializer_class = ProductSerializer

class ProviderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
