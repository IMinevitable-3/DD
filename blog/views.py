from django.shortcuts import render 
from .models import Article
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages 
from oauthen.models import User
from django.utils.text import slugify
def blog_view(request):
    articles = Article.objects.all() 
    return render(request,'blog.html',{'articles':articles})  

def asked_article_view(request,article_asked) :
    article = Article.objects.get(article_head=article_asked)
    return render(request,'blog_detailed.html' , context={'article_asked' : article})

@login_required()
def write_blog_view(request,user):
    if request.method == "POST":
        title =  slugify(request.POST['title'])  
        content = request.POST['content'] 
        now = datetime.datetime.now()
        usr = User.objects.get(username=user) 
        article = Article(user_written=usr , Date_written=now, article_head=title,content=content)
        article.save() 
        messages.info(request,"new blog was added") 
        return render(request,"write_blog.html") 

    return render(request , "write_blog.html") 
