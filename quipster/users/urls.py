from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('recover-account/', recover_account, name='recover-account'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]
