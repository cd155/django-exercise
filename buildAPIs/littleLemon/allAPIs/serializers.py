from .models import Book, Category
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'inventory', 'category']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory': {'min_value': 0},
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
