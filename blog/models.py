from django.db import models
from oauthen.models import User 
class Article(models.Model):
    user_written = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_written = models.DateTimeField(auto_now_add=True)
    article_head = models.SlugField(max_length=30) 
    content      = models.TextField()
