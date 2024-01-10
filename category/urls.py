from django.urls import path

<<<<<<< HEAD
from category.views import topics_view, category_topics, search_result
from .views import add_product, list, edit, product_delete, product_detail
=======
from category.views import topics_view, category_topics, search_result, product_detail
from .views import add_product, product_list, product_edit, product_delete
>>>>>>> 219d2a14fb43233bc83c3aee05265675b92a6ed6
from category import views

urlpatterns = [
    path('topics/', topics_view, name='topics'),
    path('topics/<slug:category_slug>/', category_topics, name='category_topics'),
    path('search_result/', search_result, name='search_result'),
    path('<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
<<<<<<< HEAD
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),


    # CRUD URLs
    path('add_product/', add_product, name='add_product'),
    path('list/', list, name='list'),
    path('edit/<int:product_id>/', edit, name='edit'),
    path('product_delete/<int:product_id>/', product_delete, name='product_delete'),

=======

    # CRUD URLs
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
    path('product_list_default/', product_list, name='product_list_default'),
    path('product_edit/<int:pk>/', product_edit, name='product_edit'),
    path('product_delete/<int:pk>/', product_delete, name='product_delete'),
>>>>>>> 219d2a14fb43233bc83c3aee05265675b92a6ed6
]
