from django.urls import path
from mynewapp import views

urlpatterns = [
    path('', views.mynewapp, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('service1/', views.service1, name='service1'),
    path('aimag/', views.aimag, name='aimag'),
    path('appointment/', views.appointment, name='appointment'),
    path('blog/', views.blog, name='blog'),
    path('shop', views.shop, name='shop'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('horoo/', views.horoo, name='horoo'),
    path('zahialagch/', views.zahialagch, name='zahialagch')
    # Other URL patterns
]
