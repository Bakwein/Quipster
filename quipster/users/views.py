from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User

from django.core.handlers.wsgi import WSGIRequest

from .models import TwitterUser
from posts.models import Tweet

# Create your views here.

def sign_in(request: WSGIRequest):
    if all(key in request.POST for key in ['username', 'password']) is False:
        return render(request, 'users/login.html', {'error': 'Geçersiz parametre girildi', 'username': ''})

    username = request.POST['username']
    password = request.POST['password']

    if username == '' or password == '':
        return render(request, 'users/login.html', {'error': 'Geçersiz kullanıcı adı veya şifre', 'username': username})

    user = authenticate(request, username=username, password=password)

    if user is None:
        return render(request, 'users/login.html', {'error': 'Geçersiz kullanıcı adı veya şifre', 'username': username})
    
    login(request, user)

    return redirect('index')

def sign_up(request: WSGIRequest):
    if all(key in request.POST for key in ['username', 'password', 'confirm-password', 'first-name', 'surname']) is False:
        return render(request, 'users/register.html')
    
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first-name']
    surname = request.POST['surname']
    repassword = request.POST['confirm-password']

    if username == '' or password == '' or first_name == '' or surname == '' or repassword == '':
        return render(request, 'users/register.html')

    if password != repassword:
        return render(request, 'users/register.html', {'error': 'Passwords do not match'})
    
    if User.objects.filter(username=username).exists():
        return render(request, 'users/register.html', {'error': 'Username already exists'})
    
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=surname)
    user.save()

    twitter_user = TwitterUser.objects.create(user=user)
    twitter_user.save()

    return redirect('login')

def render_register(request: WSGIRequest):
    if request.method == 'POST':
        return sign_up(request)


    return render(request, 'users/register.html')

def render_login(request: WSGIRequest):
    if request.method == 'POST':
        return sign_in(request)

    return render(request, 'users/login.html')

def recover_account(request: WSGIRequest):
    return render(request, 'users/recover-account.html')

def render_logout(request: WSGIRequest):
    logout(request)

    return redirect('login')

def profile(request: WSGIRequest):
    if request.user.is_authenticated is False:
        return redirect('login')
    
    twitter_user = TwitterUser.objects.get(user=request.user)
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'twitter_user': twitter_user,
        'tweets': tweets
    }

    return render(request, 'users/profile.html', context)