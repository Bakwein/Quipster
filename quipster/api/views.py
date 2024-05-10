from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from posts.models import Tweet
from users.models import TwitterUser
from django.contrib.auth.models import User

from django.views.decorators.http import require_http_methods
import json

# Create your views here.

@require_http_methods(["POST"])
@login_required
def like(request: WSGIRequest):
    try:
        data = json.loads(request.body)

        tweet_id = data["tweet_id"]
        tweet = Tweet.objects.get(id=tweet_id)
    except:
        return JsonResponse({'status': 'error', 'message': 'Tweet not found'}, status=404)
    
    is_liked = False

    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
        is_liked = True

    return JsonResponse({'status': 'success', 'is_liked': is_liked, 'like_count': tweet.likes.count()}, status=200)

@require_http_methods(["POST"])
@login_required
def follow(request: WSGIRequest):
    current_user = request.user
    current_twitter_user = TwitterUser.objects.get(user=current_user)
    
    try:
        data = json.loads(request.body)

        uid = data["uid"]
        user = User.objects.get(id=uid)
        twitter_user = TwitterUser.objects.get(user=user)
    except:
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)
    
    if user.username in current_twitter_user.get_followings():
        return JsonResponse({'status': 'error', 'message': 'This user is already being followed'}, status=409)
    
    current_twitter_user.following.add(user)
    
    return JsonResponse({'status': 'success', 'followers_count': len(twitter_user.get_followers())}, status=200)

@require_http_methods(["POST"])
@login_required
def unfollow(request: WSGIRequest):
    current_user = request.user
    current_twitter_user = TwitterUser.objects.get(user=current_user)
    
    try:
        data = json.loads(request.body)

        uid = data["uid"]
        user = User.objects.get(id=uid)
        twitter_user = TwitterUser.objects.get(user=user)
    except:
        return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)
    
    if user.username not in current_twitter_user.get_followings():
        return JsonResponse({'status': 'error', 'message': 'This user is already unfollowed'}, status=409)
    
    current_twitter_user.following.remove(user)
    
    return JsonResponse({'status': 'success', 'followers_count': len(twitter_user.get_followers())}, status=200)