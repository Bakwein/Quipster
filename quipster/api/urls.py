from django.urls import path
from .views import *

urlpatterns = [
    path('like', like, name='like'),
]
