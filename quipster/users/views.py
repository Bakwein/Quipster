from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User

from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404

from .models import TwitterUser
from posts.models import Tweet
from .forms import TwitterUserForm
from .langs import context2
# Create your views here.

def sign_in(request: WSGIRequest):
    #cookie
    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context2[language]

    if all(key in request.POST for key in ['username', 'password']) is False:
        return render(request, 'users/login.html', {'error': 'Geçersiz parametre girildi', 'username': '',"context": language_context})

    username = request.POST['username']
    password = request.POST['password']

    if username == '' or password == '':
        return render(request, 'users/login.html', {'error': 'Geçersiz kullanıcı adı veya şifre', 'username': username,"context": language_context})

    user = authenticate(request, username=username, password=password)

    if user is None:
        return render(request, 'users/login.html', {'error': 'Geçersiz kullanıcı adı veya şifre', 'username': username,"context": language_context})
    
    login(request, user)

    return redirect('posts:index')

def sign_up(request: WSGIRequest):
    #cookie
    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context2[language]

    if all(key in request.POST for key in ['username', 'password', 'confirm-password', 'first-name', 'surname']) is False:
        return render(request, 'users/register.html',{"context": language_context})
    
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first-name']
    surname = request.POST['surname']
    repassword = request.POST['confirm-password']

    if username == '' or password == '' or first_name == '' or surname == '' or repassword == '':
        return render(request, 'users/register.html',{"context": language_context})

    if password != repassword:
        return render(request, 'users/register.html', {'error': 'Passwords do not match',"context": language_context})
    
    if User.objects.filter(username=username).exists():
        return render(request, 'users/register.html', {'error': 'Username already exists',"context": language_context})
    
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=surname)
    user.save()

    twitter_user = TwitterUser.objects.create(user=user)
    twitter_user.save()

    return redirect('users:login')

def render_register(request: WSGIRequest):
     #cookie
    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context2[language]
    
    if request.method == 'POST':
        return sign_up(request)

    return render(request, 'users/register.html',{"context": language_context})

def render_login(request: WSGIRequest):
    #cookie
    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context2[language]

    if request.method == 'POST':
        return sign_in(request)

    return render(request, 'users/login.html',{"context": language_context})

def recover_account(request: WSGIRequest):
    #cookie
    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context2[language]

    return render(request, 'users/recover-account.html',{"context": language_context})

def render_logout(request: WSGIRequest):
    logout(request)

    return redirect('users:login')

def profile(request: WSGIRequest, username: str):
    
    #cookie
    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context2[language]

    if request.user.is_authenticated is False:
        return redirect('users:login')
    
    if request.method == "POST":
        return edit_profile(request)
    
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404("User does not exist")
    
    twitter_user = TwitterUser.objects.get(user=user)
    tweets = Tweet.objects.filter(user=twitter_user).order_by('-created_at')

    tweet_count = Tweet.get_tweets_count(user=twitter_user)

    context = {
        'twitter_user': twitter_user,
        'tweets': tweets,
        'username': username,
        "context2": language_context,
        'tweet_count': tweet_count
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

    full_name = request.POST.get('full-name', "").split(' ')

    username = request.POST.get('username', user.username)
    
    first_name = full_name[0]
    last_name = full_name[1] if len(full_name) > 1 else ""

    if username != user.username:
        if User.objects.filter(username=username).exists() is False:
            user.username = username

    if first_name != user.first_name or first_name != "":
        user.first_name = first_name

    if last_name != user.last_name or last_name != "":
        user.last_name = last_name

    user.save()
    
    return redirect(url)
def click_view(request):
    return render(request, 'users/click.html')