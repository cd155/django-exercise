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
    # path('categories', views.CategoriesView.as_view()),
    path('categories/<int:pk>', views.SingleCategoryView.as_view(), name='category-detail'),

    ## for function views
    # path('menu-items', views.menu_items),
    # path('menu-items/<int:id>', views.single_item),
    # path('category/<int:pk>', views.category_detail, name='category-detail')
]
