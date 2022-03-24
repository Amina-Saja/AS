from django.db import models

# Create your models here.
class users(models.Model):

    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    email=models.CharField(max_length=25)
    address=models.CharField(max_length=50)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    confirmpassword=models.CharField(max_length=15)
    
    