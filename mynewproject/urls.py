from django.conf.urls.static import static
from django.urls import path, include
from accounts import aimag
from mynewapp import views
from django.contrib import admin

from mynewproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mynewapp, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('service1/', views.service1, name='service1'),
    path('aimag/', aimag.aimagSumJagsaalt, name='aimagSumJagsaalt'),

    path('blog/', views.blog, name='blog'),
    path('shop', views.shop, name='shop'),
    path('forgetpass/', views.forgetpass, name='forgetpass'),
    path('horoo/', views.horoo, name='horoo'),
    path('huduu/', views.huduu, name='huduu'),
    path('bayangol/', views.bayangol, name='bayangol'),
    path('uilchilgee1/', views.uilchilgee1, name='uilchilgee1'),

    path('', include('accounts.urls')),
    path('', include('category.urls')),
    path('', include('listings.urls')),

    # Other URL patterns
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
