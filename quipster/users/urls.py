from django.urls import path
from .views import *
from . import views
app_name = 'users'

urlpatterns = [
    path('register/', render_register, name='register'),
    path('login/', render_login, name='login'),
    path('recover-account/', recover_account, name='recover-account'),
    path('logout/', render_logout, name='logout'),
    path('profile/<str:username>', profile, name='profile'),
    path('users/profile/click/', views.click_view,name='users_profile_click'),
]