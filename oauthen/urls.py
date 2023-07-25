from django.contrib import admin
from django.urls import path , include 
from . import views
urlpatterns = [
    path('',views.home_view,name = "home_view"),
    path('login',views.login_view,name="login_view"),
    path('forgot-password' , views.forgot_password_view,name="forgot_password_view"),
    path('signup',views.signup_view,name="signup_view"),
    path('logout',views.logout_view,name="logout_view"),
    path('profile',views.profile_view,name="profile" ),
]
