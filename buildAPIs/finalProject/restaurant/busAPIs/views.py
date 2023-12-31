from datetime import datetime
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
    UserSerializer, CartSerializer, OrderSerializer


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
            username = request.data['username']
            # if not find return 404
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name="Manager")
            managers.user_set.add(user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
class SingleManagerView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            user = get_object_or_404(User, pk=pk)
            managers = Group.objects.get(name="Manager")
            managers.user_set.remove(user)
            return Response(status=status.HTTP_200_OK)
        else:
            Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
class DeliveryCrewView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery crew')
    serializer_class = UserSerializer

    def get(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return super().get(request)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            username = request.data['username']
            # if not find return 404
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name="Delivery crew")
            managers.user_set.add(user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
class SingleDeliveryCrewView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            user = get_object_or_404(User, pk=pk)
            managers = Group.objects.get(name="Delivery crew")
            managers.user_set.remove(user)
            return Response(status=status.HTTP_200_OK)
        else:
            Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
class CartView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = CartSerializer

    def get(self, request):
        if request.user.groups.filter(name='Customer').exists():
            self.queryset = Cart.objects.filter(user=request.user.id)
            items = self.queryset.values()
            if len(items) < 1:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return super().get(request)
        return Response("Sorry, you are not a customer.", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if request.user.groups.filter(name='Customer').exists():
            self.kwargs['user'] = request.user.id
            return super().post(request)
        return Response("Sorry, you are not a customer.", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        self.queryset = Cart.objects.filter(user=request.user.id)
        if request.user.groups.filter(name='Customer').exists():
            self.queryset.delete()
            return Response("Your cart cleared.", status=status.HTTP_200_OK)
        return Response("Sorry, you are not a customer.", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class OrdersView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get(self, request):
        if request.user.groups.filter(name='Manager').exists():
            self.queryset = Order.objects.all()
            return super().get(request)
        elif request.user.groups.filter(name='Customer').exists():
            self.queryset = Order.objects.filter(user=request.user)
            return super().get(request)
        elif request.user.groups.filter(name='Delivery crew').exists():
            self.queryset = Order.objects.filter(delivery_crew=request.user)
            return super().get(request)
        else:
            return Response("Unauthorized", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if request.user.groups.filter(name='Customer').exists():
            # get all cart items,
            items = Cart.objects.filter(user=request.user.id)

            if len(items) == 0:
                return Response("Cart is empty.", status=status.HTTP_400_BAD_REQUEST)

            # create a new order
            total = 0
            for item in items:
                total += item.price

            my_order = Order(user=request.user,
                             status=True,
                             total=total,
                             date=datetime.now())
            my_order.save()

            # add order items (link to my_order)
            for item in items:
                print(item.unit_price)

                my_order_item = OrderItem(order=my_order,
                                          menuitem=item.menuitem,
                                          quantity=item.quantity,
                                          unit_price=item.unit_price,
                                          price=item.price)
                my_order_item.save()

            # clear the cart
            items.delete()

            return Response("Everything is all set.", status=status.HTTP_201_CREATED)

        return Response("Sorry, you are not a customer.", status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, pk):
        if request.user.groups.filter(name='Customer').exists():
            my_order = get_object_or_404(Order, pk=pk)
            if request.user.id == my_order.user.id:
                return super().get(request)
            else:
                return Response("Not your order", status=status.HTTP_401_UNAUTHORIZED)
        return Response("Unauthorized", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            return super().put(request)
        return Response("Unauthorized", status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            return super().patch(request)
        if request.user.groups.filter(name='Delivery crew').exists():
            if 'delivery_crew' in request.data:
                return Response("can't update this field", status=status.HTTP_400_BAD_REQUEST)
            return super().patch(request)
        return Response("Unauthorized", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            return super().delete(request)
        return Response("Unauthorized", status=status.HTTP_400_BAD_REQUEST)
