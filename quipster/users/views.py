from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User

from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404

from .models import TwitterUser
from posts.models import Tweet
from .forms import TwitterUserForm

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

    return redirect('posts:index')

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

    return redirect('users:login')

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

    return redirect('users:login')

def profile(request: WSGIRequest, username: str):
    if request.user.is_authenticated is False:
        return redirect('users:login')
    
    if request.method == "POST":
        return edit_profile(request)
    
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404("User does not exist")
    
    twitter_user = TwitterUser.objects.get(user=user)
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'twitter_user': twitter_user,
        'tweets': tweets,
        'username': username
    }

    return render(request, 'users/profile.html', context)

def edit_profile(request: WSGIRequest):
    user = request.user
    twitter_user = TwitterUser.objects.get(user=user)

    url = f"/users/profile/{user.username}"

    data = {
        'description': request.POST['description'] if 'description' in request.POST else twitter_user.description,
    }

    form = TwitterUserForm(data, request.FILES, instance=twitter_user)

    if form.is_valid():
        form.save()

    full_name = request.POST.get('full-name', user.get_full_name()).split(' ')

    username = request.POST.get('username', user.username)
    first_name = full_name[0]
    last_name = full_name[1]

    if username != user.username:
        if User.objects.filter(username=username).exists() is False:
            user.username = username

    if first_name != user.first_name:
        user.first_name = first_name

    if last_name != user.last_name:
        user.last_name = last_name

    user.save()
    
    return redirect(url)