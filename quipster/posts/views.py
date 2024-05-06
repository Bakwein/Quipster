from django.shortcuts import render
from users.models import TwitterUser

# Create your views here.

def index(request):
    if request.user.is_authenticated is False:
        return render(request, 'users/login.html')
    
    twitter_user = TwitterUser.objects.get(user=request.user)

    return render(request, 'pages/index.html', {'twitter_user': twitter_user})