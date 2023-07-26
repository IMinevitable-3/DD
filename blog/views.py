from django.shortcuts import render ,get_object_or_404
from .models import Article
def blog_view(request):
    articles = Article.objects.all() 
    return render(request,'blog.html',{'articles':articles})  

def asked_article_view(request,article_asked) :
    article = Article.objects.get(article_head=article_asked)
    return render(request,'blog_detailed.html' , context={'article_asked' : article})