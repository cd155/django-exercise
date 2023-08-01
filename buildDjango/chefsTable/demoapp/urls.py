from django.urls import path
from . import views

app_name = 'demoapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('drinks/<str:drink>', views.drinks, name='drinks'),
    path('http/', views.httpObject, name='http'),
    path('query/', views.query, name='query'),
    path("showForm/", views.showForm, name="showForm"),
    path("showForm/getForm/", views.getForm, name='getForm'),
    path("myReverse/", views.myReverse, name='myReverse'),
]
