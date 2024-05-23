from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TwitterUser(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    banner_image = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    description = models.TextField(max_length=200, blank=True, default="")
    
    def get_followings(self):
        return [user.username for user in self.following.all()]

    def get_followers(self):
        return [user.user.username for user in TwitterUser.objects.filter(following=self.user)]

    def __str__(self):
        return self.user.username