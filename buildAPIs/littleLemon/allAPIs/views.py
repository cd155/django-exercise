from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated
from .throttles import ThreeCallsPerMinute

from .models import Book, Category, Rating
from .forms import BookForm
from .serializers import BookSerializer, CategorySerializer, RatingSerializer


@api_view(['GET', 'POST'])
def home(request):
    return Response('good', status=status.HTTP_200_OK)


@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            not_exist = Book.objects.filter(
                title=form.data['title'],
                author=form.data['author']).count() == 0
            if not_exist:
                form.save()
                return JsonResponse(form.data, status=201)
            else:
                return JsonResponse({'message': 'record already exists'})
        else:
            return JsonResponse(
                {'error': 'true', 'message': 'required field missing'},
                status=400)


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # change look up file, defaults to 'pk'
    lookup_field = 'title'


class MenuItemsView(generics.ListCreateAPIView):
    # more efficient for relation in two models
    queryset = Book.objects.select_related('category').all()
    serializer_class = BookSerializer

    # Only include database side field name not Serializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

    # conditional throttling
    def get_throttles(self):
        if self.request.method == 'GET':
            self.throttle_classes = [AnonRateThrottle, UserRateThrottle]
        else:
            self.throttle_classes = [ThreeCallsPerMinute]
        return [throttle() for throttle in self.throttle_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# function view for menu_items


@api_view()
def menu_items(request):
    if request.method == 'GET':
        items = Book.objects.all()

        # serialize the object to string
        serialized_item = BookSerializer(
            items, many=True, context={'request': request})
        return Response(serialized_item.data)
    if request.method == 'POST':

        # deserialize string to the object
        serialized_item = BookSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view()
def single_item(request, pk):
    item = Book.objects.get(pk=pk)
    serialized_item = BookSerializer(item, context={'request': request})
    return Response(serialized_item.data)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)


class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if (self.request.method == 'GET'):
            return []
        return [IsAuthenticated()] # need a token to do a post call
