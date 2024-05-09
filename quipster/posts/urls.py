from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('oauth_login/', oauth_login, name='oauth_login'),
    path('', index, name='index'),

]
