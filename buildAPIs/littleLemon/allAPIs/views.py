from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Book
from .forms import BookForm
from .serializers import BookSerializer


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
