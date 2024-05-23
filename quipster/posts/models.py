from django.db import models
from users.models import TwitterUser

# Create your models here.

class Tweet(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(TwitterUser, related_name='likes', blank=True)
    images = models.TextField(blank=True, default="")
    replied_tweet = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
    def get_comments(self):
        return Tweet.objects.filter(replied_tweet=self)
    
    def get_comments_count(self):
        return Tweet.objects.filter(replied_tweet=self).count()
    
    def get_likes(self):
        return self.likes.count()
    
    def is_comment(self):
        return self.replied_tweet != None
    
    def get_images(self):
        return [image.strip() for image in self.images.split("\n")]
    
    @classmethod
    def get_tweets_count(cls, user: TwitterUser):
        return cls.objects.filter(user=user).count()
    
    @classmethod
    def get_latest_tweets(cls, user: TwitterUser, count: int = 5):
        return cls.objects.filter(user=user, replied_tweet=None).order_by('-created_at')[:count]