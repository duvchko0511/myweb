from django.urls import path

from category import views
from .views import add_product, topics_view

urlpatterns = [
    path('topics/', topics_view, name='topics'),
    path('topics/<slug:category_slug>/', views.category_topics, name='category_topics'),
    path('search_result/', views.search_result, name='search_result'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
]
