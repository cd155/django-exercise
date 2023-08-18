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
    # category = CategorySerializer()

    category = serializers.HyperlinkedRelatedField(
        # used for model instance lookups when validating the field input.
        # queryset=Category.objects.all(),

        # bug: have to specify the app name in Hyperlinked
        view_name='allAPIs:category-detail',

        read_only=True
    )

    # make category_id writable but not visible
    category_id = serializers.IntegerField(write_only=True)

    # assign inventory field to stock
    stock = serializers.IntegerField(source='inventory')

    # assign price_after_tax with a method
    price_after_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price',
                  'stock', 'category', 'price_after_tax', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory': {'min_value': 0},
        }

    def calculate_tax(self, product: Book):
        return product.price * Decimal(1.13)
