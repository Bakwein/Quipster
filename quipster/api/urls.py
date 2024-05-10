from django.urls import path
from .views import *

urlpatterns = [
    path('like', like, name='like'),
    path('follow', follow, name='follow'),
    path('unfollow', unfollow, name='unfollow')
]
