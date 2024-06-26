from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from posts.models import Tweet
from users.models import TwitterUser
from django.contrib.auth.models import User

from django.views.decorators.http import require_http_methods
import json
import re

from .generate_sentence import generate_sentencefonk
from django.utils.safestring import mark_safe
from django.utils.html import escape

from .gallery_manager import upload_images
from django.conf import settings

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
    
    sender_user = TwitterUser.objects.get(user=request.user)

    if sender_user in tweet.likes.all():
        tweet.likes.remove(sender_user)
    else:
        tweet.likes.add(sender_user)
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

@require_http_methods(["POST"])
@login_required
def post(request: WSGIRequest):
    current_user = request.user
    current_twitter_user = TwitterUser.objects.get(user=current_user)

    try:
        data = request.POST
        files = request.FILES

        content: str = data.get("content")

        if content is None:
            return JsonResponse({'status': 'error', 'message': 'Error'}, status=403)
        
        images = files.getlist("tweet-images")

        content = escape(content)
        
        content = content.replace("\n", "<br>")
        content = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', content)
        content = re.sub(r'\_(.*?)\_', r'<i>\1</i>', content)
        content = re.sub(r'(https?:\/\/\S+|www\.\S+|\b\w+\.[a-zA-Z]{2,}\b)', '<a href="\g<0>" style="color: rgb(59 130 246);">\g<0></a>', content)
        content = re.sub(r'\```(.*?)\```', r'<code>\1</code>', content)

        tweet = Tweet.objects.create(user=current_twitter_user, content=content)
        
        dirname = f"{current_user.username}_{current_user.id}"
        uploaded_images = []

        if len(images) > 0:
            uploaded_images = upload_images(dirname, tweet.id, images)
            tweet.images = "\n".join(uploaded_images)

        tweet.save()
    except:
        return JsonResponse({'status': 'error', 'message': 'Error'}, status=403)
    
    return JsonResponse({'status': 'success', "content": content, "tweet_id": tweet.id, "created_at": tweet.created_at, "uploaded_images": uploaded_images}, status=200)

@require_http_methods(["POST"])
@login_required
def comment(request: WSGIRequest):
    current_user = request.user
    current_twitter_user = TwitterUser.objects.get(user=current_user)

    try:
        data = json.loads(request.body)

        tweet_id: str = data["tweet_id"]
        content: str = data["content"]
        
        content = escape(content)
        
        content = content.replace("\n", "<br>")
        content = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', content)
        content = re.sub(r'\_(.*?)\_', r'<i>\1</i>', content)
        content = re.sub(r'(https?:\/\/\S+|www\.\S+|\b\w+\.[a-zA-Z]{2,}\b)', '<a href="\g<0>" style="color: rgb(59 130 246);">\g<0></a>', content)
        content = re.sub(r'\```(.*?)\```', r'<code>\1</code>', content)

        replied_tweet = Tweet.objects.get(id=tweet_id)

        tweet = Tweet.objects.create(user=current_twitter_user, content=content, replied_tweet=replied_tweet)
        tweet.save()
    except:
        return JsonResponse({'status': 'error', 'message': 'Error'}, status=403)
    
    return JsonResponse({'status': 'success', "content": content, "tweet_id": tweet.id, "created_at": tweet.created_at}, status=200)

@require_http_methods(["POST"])
@login_required
def artifical_text(request):
    try:
        data = json.loads(request.body)
        text=data["text"]
        suggestion=generate_sentencefonk(text)
        #print(f"suggestion{suggestion}")   

        # İki yıldız arasındaki karakterleri almak için regex deseni
        pattern = r'\*\*(.*?)\*\*'

        # Eşleşen karakterleri bulma
        matches = re.match(pattern, suggestion)

        
        #print(matches.group(1))
        suggestion=matches.group(1)


    except:
        return JsonResponse({'status': 'error', 'message': 'Error'}, status=403)       
    return JsonResponse({"suggestion":suggestion},status=200)
