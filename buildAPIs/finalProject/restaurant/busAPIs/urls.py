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
    path('groups/delivery-crew/users', views.DeliveryCrewView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.SingleDeliveryCrewView.as_view()),
    path('cart/menu-items', views.CartView.as_view()),
    path('orders', views.OrdersView.as_view()),
    path('orders/<int:order_id>', views.SingleOrderView.as_view()),
]
