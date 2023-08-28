from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer

@api_view(['GET', 'POST'])
def home(request):
    return Response('good', status=status.HTTP_200_OK)


class MenuItemsView(generics.ListCreateAPIView):
    # more efficient for relation in two models
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer

    # Only include database side field name not Serializer
    # ordering_fields = ['price', 'inventory']
    # filterset_fields = ['price', 'inventory']
    # search_fields = ['title']