from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TwitterUser(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following')
    
    def get_followings(self):
        return [user.username for user in self.following.all()]

    def get_followers(self):
        return [user.user.username for user in TwitterUser.objects.filter(following=self.user)]

    def __str__(self):
        return self.user.username
    
