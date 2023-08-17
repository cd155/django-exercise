from django.urls import path
from . import views

app_name = 'allAPIs'

urlpatterns = [
    path('test-books', views.books, name='books'),
    path('', views.home, name='home'),
    path('books', views.BookView.as_view()),
    path('books/<str:title>', views.SingleBookView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]
