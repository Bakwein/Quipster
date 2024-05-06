from django.db import models
from users.models import TwitterUser
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')
    is_comment = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content
    
    def get_comments(self):
        return Tweet.objects.filter(parent=self)
    
    def get_comments_count(self):
        return Tweet.objects.filter(parent=self).count()
    
    def get_likes(self):
        return self.likes.count()