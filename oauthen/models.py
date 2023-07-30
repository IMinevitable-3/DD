from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    mobile_number = models.CharField(max_length=15,null=True)
    date_of_birth = models.DateField(null=True)
    diabetic = models.BooleanField(null=True)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')],null=True)
    country = models.CharField(max_length=100,null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    mean_sugar_level = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    def __str__ (self):
        return f'{self.username}' 
    

    
class issue(models.Model) :
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(max_length=30) 
    content=models.TextField() 
    status = models.BooleanField(default=False)
    