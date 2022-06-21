from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    profpic = models.ImageField( blank=True, upload_to="images/")


