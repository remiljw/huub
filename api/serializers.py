from django.db.models import fields
from rest_framework import serializers

from api.models import DeliveredItem, Delivery, OrderItem, Order

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField('name', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField('name', read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'brand', 'brand_id', 'customer_name', 'reference', 'address', 'order_date', 'price_total']


class DeliveredItemSerializer(serializers.ModelSerializer):
    product_name = serializers.SlugRelatedField('name', read_only=True)
    class Meta:
        model = DeliveredItem
        fields = ['product_name', 'quantity']

class DeliverySerializer(serializers.ModelSerializer):
    products = DeliveredItemSerializer(many=True)
    class Meta:
        model = Delivery
        fields = ['id', 'order_id', 'shipped', 'products']

