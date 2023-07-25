from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages 
from django.db import IntegrityError
from .models import User
from .utilities import sendmail




def logout_view(request):
    logout(request) 
    return render(request,home_view) 

def profile_view(request):
    return render(request,'user.html') 
def home_view(request):
    return render(request,'index.html') 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd      = request.POST['pass']
        user = authenticate(request, username=username, password=pwd )

        if user is not None :
            login(request, user)
            return redirect(profile_view)
        else :
            messages.error(request , "bad credentials") 
            return redirect(home_view)
    return render(request,'login.html')

def forgot_password_view(request):
    if request.method == 'POST' :
        user_name= request.POST.get('username')
        try :
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            #handle message 
            return HttpResponse('user doesnt exist')
    
        new_password=sendmail(user.email)
        user.set_password(new_password)
        user.save()
        return redirect(login_view) #need to inform user about sent email 


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

