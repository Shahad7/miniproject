from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 64)
    author = models.CharField(max_length = 64)
    photo = models.ImageField(upload_to="",null=True)
    stock = models.IntegerField(blank=True,null=True)

class myuser(AbstractUser):
    user_types = (
        ('STUDENT','student'),
        ('LIBRARIAN','librarian')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    role = models.CharField(max_length=100,choices=user_types,default='STUDENT')
    USERNAME_FIELD = 'username'

class Rent(models.Model):
 #   bid = models.ForeignKey(Book,on_delete=models.CASCADE)
 #   sid = models.ForeignKey(myuser,on_delete=models.CASCADE)
    bid = models.IntegerField(blank=True,null=True)
    sid = models.IntegerField(blank=True,null=True)


