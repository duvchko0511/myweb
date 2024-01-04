from django.urls import path

from category.views import topics_view, category_topics, search_result, product_detail
from .views import add_product, product_list, product_edit, product_delete
from category import views

urlpatterns = [
    path('topics/', topics_view, name='topics'),
    path('topics/<slug:category_slug>/', category_topics, name='category_topics'),
    path('search_result/', search_result, name='search_result'),
    path('<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),

    # CRUD URLs
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
    path('product_list_default/', product_list, name='product_list_default'),
    path('product_edit/<int:pk>/', product_edit, name='product_edit'),
    path('product_delete/<int:pk>/', product_delete, name='product_delete'),
]
