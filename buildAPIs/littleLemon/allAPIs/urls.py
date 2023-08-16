from django.urls import path
from . import views

app_name = 'allAPIs'

urlpatterns = [
    path('books', views.books, name='books'),
    path('', views.home, name='home'),
]
