import requests

from django.shortcuts import render, redirect
from .models import TwitterUser
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from posts.models import Tweet

# Create your views here.

def index(request: WSGIRequest):
    if request.user.is_authenticated is False:
        return redirect("users:login")
    
    twitter_user = TwitterUser.objects.get(user=request.user)
    all_tweets = []

    all_tweets.extend(Tweet.get_latest_tweets(user=twitter_user))

    for user in twitter_user.following.all():
        tw_user = TwitterUser.objects.get(user=user)
        tweets = Tweet.get_latest_tweets(user=tw_user)

        all_tweets.extend(tweets)

    all_tweets = sorted(all_tweets, key=lambda x: x.created_at, reverse=True)

    print(all_tweets)

    return render(request, 'pages/index.html', {'twitter_user': twitter_user, "tweets": all_tweets})

def oauth_login(request: WSGIRequest):
    google_user_info = request.user.social_auth.get(provider='google-oauth2').extra_data

    response =  requests.get('https://www.googleapis.com/oauth2/v1/userinfo', headers={'Authorization': f'Bearer {google_user_info["access_token"]}'})
    if response.status_code != 200:
        return redirect('users:login')
    data = response.json()
    username = data['given_name'] + '_' + data['family_name']
    
    existed_user = User.objects.filter(username=username).first()

    if existed_user is None:
        firstname = response.json()['given_name']
        lastname = response.json()['family_name']

        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname)
        user.save()

        twitter_user = TwitterUser.objects.create(user=user)
        twitter_user.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return render(request, 'pages/index.html', {'twitter_user': twitter_user})

    login(request, existed_user, backend='django.contrib.auth.backends.ModelBackend')
    twitter_user = TwitterUser.objects.get(user=existed_user)

    return render(request, 'pages/index.html', {'twitter_user': twitter_user})