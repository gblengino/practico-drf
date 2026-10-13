from rest_framework import serializers
from .models import Product, Provider, Order, OrderItem

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"
        read_only_fields = ["id", "created_at"]

class ProductPublicSerializer(serializers.ModelSerializer):

    provider = ProviderSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "provider"
        ]
        read_only_fields = ["id"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "cost",
            "stock",
            "provider",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'total',
            'payment_method',
            'created_at'
        ]
        read_only_fields = ['id', 'payment_method', 'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
