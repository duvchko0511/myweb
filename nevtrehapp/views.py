
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages , auth
from mynewapp.models import Nevtreh
from django.contrib.auth import authenticate, login
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

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['login-password']  # Make sure the name matches the HTML form

        # Authenticate using the 'username' field, assuming it's an email field
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard/')  # Replace 'dashboard/' with the appropriate URL after login
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login/')
    else:
        return render(request, 'login.html')