from django.urls import path, include
from mynewapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mynewapp, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('service1/', views.service1, name='service1'),
    path('aimag/', views.aimag, name='aimag'),
    path('appointment/', views.appointment, name='appointment'),
    path('blog/', views.blog, name='blog'),
    path('shop', views.shop, name='shop'),
    path('forgetpass/', views.forgetpass, name='forgetpass'),
    path('horoo/', views.horoo, name='horoo'),
    path('zahialagch/', views.zahialagch, name='zahialagch'),
    path('huduu/', views.huduu, name='huduu'),
    path('bayangol/', views.bayangol, name='bayangol'),
    path('uilchilgee1/', views.uilchilgee1, name='uilchilgee1'),

    path('', include('accounts.urls'))
 
    # Other URL patterns
]
