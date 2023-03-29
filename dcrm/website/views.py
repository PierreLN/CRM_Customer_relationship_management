from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been login!')
            return redirect('home')
        else: 
            messages.success(request, "Fail, please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout...')
    return redirect('home')
