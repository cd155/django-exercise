from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('drinks/<str:drink>', views.drinks, name='drinks'),
    path('http/', views.httpObject, name='http'),
    path('query/', views.query, name='query'),
]
