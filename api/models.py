from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class profile(models.Model):
    username = models.TextField(max_length=100)
    posts = models.DecimalField(max_digits=3, decimal_places=3)

    def __str__(self):
        return self.username

    
class Post(models.Model):
    picture  = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
