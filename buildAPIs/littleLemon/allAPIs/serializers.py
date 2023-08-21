from .models import Book, Category
from rest_framework import serializers
from decimal import Decimal
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # constraints for price
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, min_value=3)

    # convert category object to string
    # category = serializers.StringRelatedField()

    # set category to CategorySerializer
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

    ## set title constraints
    # title = serializers.CharField(
    #     max_length=255,
    #     validators=[UniqueValidator(queryset=Book.objects.all())])
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price',
                  'stock', 'category', 'price_after_tax', 'category_id']
        extra_kwargs = {            
            ## set constraints in extra_kwargs
            # 'price': {'min_value': 2},
            # 'inventory': {'min_value': 0},
            # 'stock': {'source': 'inventory', 'min_value': 0}

            # unique validator
            'title': {
                'validators': [
                    UniqueValidator(
                        queryset=Book.objects.all()
                    )
                ]
            }
        }

    def calculate_tax(self, product: Book):
        return product.price * Decimal(1.13)

    # validate method for price
    def validate_price(self, value):
        if (value < 2):
            raise serializers.ValidationError(
                'Price should not be less than 2.0')

    ## other validate method
    # def validate(self, attrs):
    #     if(attrs['price']<2):
    #         raise serializers.ValidationError('Price should not be less than 2.0')
    #     if(attrs['inventory']<0):
    #         raise serializers.ValidationError('Stock cannot be negative')
    #     return super().validate(attrs)

    # validate method for stock
    def validate_stock(self, value):
        if (value < 0):
            raise serializers.ValidationError('Stock cannot be negative')
