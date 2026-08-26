from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

@api_view(["GET", "POST"])
def products(request):
    if request.method == "GET":
        products = Product.objects.all()
        products_serialized = ProductSerializer(products, many=True)
        return Response(
            products_serialized.data,
            status=status.HTTP_200_OK
            )

    if request.method == "POST":
        new_product_serialized = ProductSerializer(data=request.data)
        if new_product_serialized.is_valid():
            new_product_serialized.save()
            return Response(
                {"message":"Product created"},
                status=status.HTTP_201_CREATED
                )

@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "GET":
        product_serialized = ProductSerializer(product)
        return Response(
            product_serialized.data,
            status=status.HTTP_200_OK
            )

    if request.method == "PUT":
        product_serialized = ProductSerializer(product, data=request.data)
        if product_serialized.is_valid():
            product_serialized.save()
            return Response(
                {"message":"Product updated"},
                status=status.HTTP_200_OK
            )

    if request.method == "DELETE":
        product.is_active = False
        product.save()
        return Response(
            {"message":"Product deleted"},
            status=status.HTTP_200_OK
        )