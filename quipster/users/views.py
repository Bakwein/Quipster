from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def recover_account(request):
    return render(request, 'users/recover-account.html')

def logout(request):
    pass
    #return render(request, 'users/logout.html')

def profile(request):
    pass