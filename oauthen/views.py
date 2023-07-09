from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages 
from django.db import IntegrityError
from .models import User

def logout_view(request):
    logout(request) 
    return render(request,home_view) 
def home_view(request):
    return render(request,'index.html') 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd      = request.POST['pass']
        user = authenticate(request, username=username, password=pwd )

        if user is not None :
            login(request, user)
            print('loggedint') 
            return render(request,'user.html')
        else :
            messages.error(request , "bad credentials") 
            print("here")
            return redirect(home_view)
    return render(request,'login.html')

def forgot_password_view(request):
    return render(request,'forgot_password.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['pass1']
        confirm = request.POST['pass2']
        email = request.POST['email']

        if password != confirm:
            messages.error("password and confirm password must match")
            return render(request, 'signup.html')
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error("username already taken") 
            return render(request, 'signup.html')
        
        login(request, user)
        return HttpResponseRedirect(reverse('home_view')) 

    return render(request,'signup.html') 

