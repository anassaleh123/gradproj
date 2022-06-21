from django.db import models

# Create your models here.

class braceletsettings(models.Model):
    userid = models.IntegerField(default=True,primary_key=True)
    how_to_use = models.CharField(max_length=300,default=True)
    edit_name = models.CharField(default=True,max_length=40)
     