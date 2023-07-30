from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('drinks/<str:drink>', views.drinks, name='drinks'),
]
