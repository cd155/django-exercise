from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer,\
    UserSerializer


@api_view(['GET', 'POST'])
def home(request):
    return Response('good', status=status.HTTP_200_OK)


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@permission_classes([IsAuthenticated])
class MenuItemsView(generics.ListCreateAPIView):
    # more efficient for relation in two models
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer

    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return super().post(request)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def put(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            return super().put(request)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            return super().patch(request)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            return super().delete(request)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
class ManagersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer

    def get(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return super().get(request)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return super().post(request)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
class SingleManagerView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return super().delete(request)
        else:
            Response(status=status.HTTP_403_FORBIDDEN)
