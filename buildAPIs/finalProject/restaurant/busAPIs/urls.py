from django.urls import path, include
from . import views

app_name = 'busAPIs'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('categories', views.CategoriesView.as_view()),
    path('groups/manager/users', views.ManagersView.as_view()),
    path('groups/manager/users/<int:pk>', views.SingleManagerView.as_view()),
]
