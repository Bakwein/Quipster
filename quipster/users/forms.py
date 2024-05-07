from django import forms
from django.contrib.auth.models import User
from .models import TwitterUser

class TwitterUserForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['profile_picture', 'banner_image', 'description']
