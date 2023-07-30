from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect , HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages 
from django.db import IntegrityError
from .models import User , issue ,Food
from .utilities import sendmail
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request) 
    return redirect(home_view)

@login_required(login_url="/login")
def dashboard_view(request):
    return render(request,'user.html',context={}) 

def home_view(request):
    return render(request,'index.html') 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd      = request.POST['pass']
        user = authenticate(request, username=username, password=pwd )

        if user is not None :
            login(request, user)
            return redirect(dashboard_view)
        else :
            messages.error(request , "bad credentials") 
            return redirect(login_view)
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
        messages.info(request,"please check your registered mail for new password")
        return redirect(login_view)


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
@login_required() 
def settings_view(request , name):
    try :
        query = User.objects.get(username=name) 
    except :
        return redirect(home_view) 
    
    if request.method == 'POST':
        user = get_object_or_404(User, username=name)
        try :
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.mobile_number = request.POST.get('mobile_number')
            user.date_of_birth = request.POST.get('date_of_birth')
            user.diabetic = request.POST.get('diabetic') == 'yes'
            user.gender = request.POST.get('gender')
            user.country = request.POST.get('country')
            user.height = request.POST.get('height')
            user.weight = request.POST.get('weight')
            user.mean_sugar_level = request.POST.get('mean_sugar_level')
            user.username = name 
        except:
            messages.error(request,"enter valid data") 
            return render(request,'profile.html' , context={"user":query})  

        user.save()
        messages.success(request,"profile updated") 
        return render(request,'profile.html' , context={"user":query})  
        

    return render(request,'profile.html',context={"user":query}) 

@login_required()
def issue_view(request,name):
    if request.method == "POST" :
        usr = User.objects.get(username=name) 
        title = request.POST["issues"] 
        desc  =request.POST["content"] 
        user_issue = issue(author=usr,title=title,content=desc) 
        user_issue.save() 
        messages.success(request,"issue submitted successfully")
        return redirect(dashboard_view) 

    return render(request , "issue.html") 

@login_required() 
def delete_acct(request,name):
    user = get_object_or_404(User, username=name) 
    user.delete() 
    messages.success(request,'account successfully deleted') 
    return redirect(home_view) 


def get_names(request):
    search = request.GET.get('search') 
    payload =[]
    if search :
        objs = Food.objects.filter(food_name__startswith=search)
        payload =[{"name":obj.food_name} for obj in objs ]
    return JsonResponse({
        'status':True,
        'payload':payload
    })


def addmeal(request,name):
    return render(request,"addmeal.html") 