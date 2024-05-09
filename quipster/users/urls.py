from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', render_register, name='register'),
    path('login/', render_login, name='login'),
    path('recover-account/', recover_account, name='recover-account'),
    path('logout/', render_logout, name='logout'),
    path('profile/', profile, name='profile'),
]
