from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from .models import TwitterUser
from posts.models import Tweet

import requests
import secrets

from django.contrib.auth.decorators import login_required
from .langs import context

# Create your views here.

@login_required(redirect_field_name="next", login_url="users:login")
def index(request: WSGIRequest):
    twitter_user = TwitterUser.objects.get(user=request.user)
    all_tweets = []

    user_tweets = Tweet.get_latest_tweets(user=twitter_user)

    all_tweets.extend(user_tweets)

    for user in twitter_user.following.all():
        tw_user = TwitterUser.objects.get(user=user)
        tweets = Tweet.get_latest_tweets(user=tw_user)

        all_tweets.extend(tweets)

    all_tweets = sorted(all_tweets, key=lambda x: x.created_at, reverse=True)

    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context[language]

    return render(request, 'pages/index.html', {
        "twitter_user": twitter_user,
        "tweets": all_tweets,
        "context2": language_context
    })

@login_required(redirect_field_name="next", login_url="users:login")
def post_details(request: WSGIRequest, tweet_id: int):
    twitter_user = TwitterUser.objects.get(user=request.user)

    try:
        tweet = Tweet.objects.get(id=tweet_id)
        comments = Tweet.objects.filter(replied_tweet=tweet).order_by('-created_at')
    except:
        return redirect("posts:index")
    
    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context[language]

    return render(request, "pages/post-details.html", { "twitter_user": twitter_user, "tweet": tweet, "comments": comments, "context2": language_context })

def oauth_login(request: WSGIRequest):
    google_user_info = request.user.social_auth.get(provider='google-oauth2').extra_data

    response =  requests.get('https://www.googleapis.com/oauth2/v1/userinfo', headers={'Authorization': f'Bearer {google_user_info["access_token"]}'})
    if response.status_code != 200:
        return redirect('users:login')
    
    data = response.json()

    given_name = data['given_name']
    family_name = data['family_name'] if "family_name" in data else ""

    username = given_name + secrets.token_hex(5)
    
    existed_user = User.objects.filter(username=username).first()

    if existed_user is None:
        user = User.objects.create_user(username=username, first_name=given_name, last_name=family_name)
        user.save()

        twitter_user = TwitterUser.objects.create(user=user)
        twitter_user.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return render(request, 'pages/index.html', {'twitter_user': twitter_user})

    login(request, existed_user, backend='django.contrib.auth.backends.ModelBackend')
    twitter_user = TwitterUser.objects.get(user=existed_user)

    return render(request, 'pages/index.html', {'twitter_user': twitter_user})

def explore(request: WSGIRequest):
    current_user = request.user
    current_twitter_user = TwitterUser.objects.get(user=current_user)

    users = User.objects.exclude(username=current_user.username).order_by("?")[:10]

    all_tweets = []
    
    for user in users:
        try:
            twitter_user = TwitterUser.objects.get(user=user)
        except:
            continue

        tweet = Tweet.objects.filter(user=twitter_user).order_by("-created_at").first()

        if tweet is not None:
            all_tweets.append(tweet)

    if "user_language" in request.COOKIES:
        language = request.COOKIES["user_language"]

        if language not in ["tr", "en", "de"]:
            language = "en"
    else:
        language = "en"

    language_context = context[language]

    return render(request, "pages/explore.html", {"twitter_user": current_twitter_user, "tweets": all_tweets, "context2": language_context})