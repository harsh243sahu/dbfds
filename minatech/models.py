from enum import auto
from django.db import models
from . models import *
from django.conf import settings

# Create your models here.

class courses(models.Model):
    name=models.CharField(max_length = 100)
    img=models.ImageField(null=True,blank=True)
    price=models.IntegerField()
    desc=models.CharField(max_length = 3000)
     
    def __str__(self):
        return self.name

class courseContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.FileField(null=True,blank=True)
    title = models.CharField(max_length=1000)
    notes = models.TextField(null=True,blank=True)
    course = models.ForeignKey('courses',on_delete=models.CASCADE)
    uploadedOn = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title



class blogs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, null=True,blank=True,default="")
    post = models.TextField(null=True,blank=True,default="")
    image = models.ImageField(null=True,blank=True,default="")
    uploadOn = models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name

