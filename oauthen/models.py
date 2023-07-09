from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.

class User(AbstractUser):
    def __str__ (self):
        return f'{self.username}' 