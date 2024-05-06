from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from .models import TwitterUser

# Create your views here.

def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']

    if username is None or username == '':
        return render(request, 'users/login.html')
    
    if password is None or password == '':
        return render(request, 'users/login.html')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('index')
    
    return render(request, 'users/login.html', {'error': 'Invalid username or password'})

def sign_up(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['confirm-password']

    if username is None or username == '':
        return render(request, 'users/register.html')
    if password is None or password == '':
        return render(request, 'users/register.html')
    if repassword is None or repassword == '':
        return render(request, 'users/register.html')

    if password != repassword:
        return render(request, 'users/register.html', {'error': 'Passwords do not match'})
    
    if User.objects.filter(username=username).exists():
        return render(request, 'users/register.html', {'error': 'Username already exists'})
    
    user = User.objects.create_user(username=username, password=password)
    user.save()

    twitter_user = TwitterUser.objects.create(user=user)
    twitter_user.save()

    return redirect('login')

def render_register(request):
    if request.method == 'POST':
        return sign_up(request)


    return render(request, 'users/register.html')

def render_login(request):
    if request.method == 'POST':
        return sign_in(request)

    return render(request, 'users/login.html')

def recover_account(request):
    return render(request, 'users/recover-account.html')



def render_logout(request):
    logout(request)    
    return redirect('login')

def profile(request):
    pass