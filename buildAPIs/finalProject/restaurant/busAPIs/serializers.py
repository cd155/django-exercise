from rest_framework import serializers

from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User
from rest_framework.response import Response


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    order_items = serializers.SerializerMethodField(read_only=True)

    def get_order_items(self, order: Order):
        order_items = OrderItem.objects.filter(order_id=order.id)
        serialized_item = OrderItemSerializer(order_items, many=True)
        return serialized_item.data

    class Meta:
        model = Order
        fields = ['pk', 'user', 'delivery_crew', 'status', 'total',
                  'date', 'order_items']
