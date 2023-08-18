from .models import Book, Category
from rest_framework import serializers
from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # convert category object to strin
    # category = serializers.StringRelatedField()

    # set full category
    category = CategorySerializer()

    # assign inventory field to stock
    stock = serializers.IntegerField(source='inventory')

    # assign price_after_tax with a method
    price_after_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price',
                  'stock', 'category', 'price_after_tax']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory': {'min_value': 0},
        }

    def calculate_tax(self, product: Book):
        return product.price * Decimal(1.13)
