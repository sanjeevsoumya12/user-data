from django.db import models
from django.contrib.auth.models import User 
import os

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

# class Profile(models.Model):   #add this class and the following fields
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
    
# def get_upload_path(instance, filename):
#     return 'documents/{0}/{1}'.format(instance.user.username, filename)
