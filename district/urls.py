# urls.py
from django.urls import path
from .views import duureg_list
from district import views
from .views import address_list, address_detail, address_create, address_edit, address_delete

urlpatterns = [
    # other patterns...
    path('duuregs/', duureg_list, name='duureg_list'),
    path('duuregs/<slug:duureg_slug>/', views.detail, name='detail'),
    path('duuregs/', address_list, name='address_list'),
    path('address/<int:pk>/', address_detail, name='address_detail'),
    path('address/new/', address_create, name='address_create'),
    path('address/<int:pk>/edit/', address_edit, name='address_edit'),
    path('address/<int:pk>/delete/', address_delete, name='address_delete'),
]
