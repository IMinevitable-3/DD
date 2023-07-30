from django.urls import path , include 
from . import  views
urlpatterns = [
    path('' , views.blog_view,name="blog_view" ),
    path('blog/<slug:article_asked>',views.asked_article_view,name="asked_article_view"),
    path('write/<user>',views.write_blog_view,name="write_blog_view") ,
]
