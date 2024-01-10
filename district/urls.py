# urls.py
from django.urls import path
from .views import product_list
from district import views
from .views import address_list, address_detail, address_create, address_edit, address_delete

urlpatterns = [
    # other patterns...
    path('products/', product_list, name='product_list'),
    path('products/<slug:product_slug>/', views.detail, name='detail'),
    path('', address_list, name='address_list'),
    path('address/<int:pk>/', address_detail, name='address_detail'),
    path('address/new/', address_create, name='address_create'),
    path('address/<int:pk>/edit/', address_edit, name='address_edit'),
    path('address/<int:pk>/delete/', address_delete, name='address_delete'),
]
