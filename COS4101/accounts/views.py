from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Invalid login')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')