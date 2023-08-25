from django.urls import path, include
from . import views

app_name = 'busAPIs'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
