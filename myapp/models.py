from django.db import models

# Create your models here.
class users(models.Model):

    name=models.CharField(max_length=30)
    email=models.CharField(max_length=25)
    phone=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    
    