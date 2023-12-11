from django.shortcuts import render
from django.http import HttpResponse

def mynewapp(request):
    # Your view logic here
    return render(request, 'index.html')   
    
def services(request):
    # index хуудсанд ажиллах кодыг энд бичнэ
    return render(request, 'services.html')

def about(request):
    # about хуудсанд ажиллах кодыг энд бичнэ
    return render(request, 'about.html')

def contact(request):
    # contact хуудсанд ажиллах кодыг энд бичнэ
    return render(request, 'contact.html')
def service1(request):
    return render(request, 'service1.html')
def aimag(request):
    return render(request, 'aimag.html')
def appointment(request):
    return render(request, 'appointment.html')
def blog(request):
    return render(request, 'blog.html')
def shop(request):
    return render(request, 'shop.html')

def signup(request):
    return render(request, 'signup')
def horoo(request):
    return render(request, 'khoroo/horoo.html')
def zahialagch(request):
    return render(request, 'uilajillagaa/zahialagch.html')
def huduu(request):
    return render(request, 'hayg/huduu.html')
def bayangol(request):
    return render(request, 'duureg/bayangol.html')
def uilchilgee1(request):
    return render(request, 'turiin/uilchilgee1.html')

def forgetpass(request):
    return render(request, 'account/forgetpass.html')
