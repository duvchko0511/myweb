from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages , auth
from mynewapp.models import Nevtreh

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken!')
                return redirect('signup/')
            else:
                user = User.objects.create_user(
                    name=name,
                    lastname=lastname,
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Nevtreh.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()

                messages.success(request, 'Registration successful!')
                return redirect('register1/')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup/')
    else:
        return render(request, 'register1.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        User = auth (email=email, password=password)
    return render(request, 'login.html')