from django.urls import path

from category import views
from .views import topics_view

urlpatterns = [
    # other patterns...
    path('topics/', topics_view, name='topics'),
    path('search_result', views.search_result, name='search_result'),
    path('<slug:category_slug>/<slug:product_slug>', views.product_detail, name='product_detail'),
    path('topics/<slug:category_slug>/', views.topics, name='topics'),
]
