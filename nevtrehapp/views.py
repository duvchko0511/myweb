from django.shortcuts import render
from django.http import HttpResponse

def mynewapp(request):
    # Your view logic here
    return render(request, 'login.html')
# Create your views here.
