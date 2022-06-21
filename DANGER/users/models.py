from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    address = models.TextField(max_length=200)
    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)
     