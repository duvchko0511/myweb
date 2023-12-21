from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),            # URL for the listings index
    path('<int:listing_id>/', views.listing, name='listing'),  # URL for a single listing
    path('index/', views.search, name='index'),       # URL for the search functionality
]
