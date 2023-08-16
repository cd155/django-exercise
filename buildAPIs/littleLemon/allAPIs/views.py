from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Book
from .forms import BookForm

# Create your views here.


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
