from django.shortcuts import render
from .models import Article
def blog_view(request):
    articles = Article.objects.all() 
    return render(request,'blog.html',{'articles':articles})  