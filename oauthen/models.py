from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    def __str__ (self):
        return f'{self.username}' 
    
class Log(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateField()
    sugar = models.IntegerField() 
    