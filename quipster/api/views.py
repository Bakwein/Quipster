from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from posts.models import Tweet

import json

# Create your views here.

def like(request: WSGIRequest):
    if request.method == "GET":
        return JsonResponse({'status': 'error', 'message': 'GET requests not allowed'}, status=405)

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

    return JsonResponse({'status': 'success', 'is_liked': is_liked, 'like_count': tweet.likes.count()})