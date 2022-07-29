from pickle import TRUE
from turtle import title
from django.db import models
from django.utils.html import format_html
from psycopg2 import Timestamp
from tinymce.models import HTMLField 
from django.contrib.auth.models import User
# Create your models here.

#Category model

class Category(models.Model):
    # only title need to be written here
    cat_id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    def __str__(self):
        return self.title
    

#Post model
class Post(models.Model):
    post_id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    # discription for first 100 words excluding img
    description=models.CharField(max_length=1000,default='')
    content= HTMLField()
    author= models.CharField(max_length=500,default='')
    
    cat=models.CharField(max_length=100,default='')
    # Timestamp=models.DateTimeField(blank=TRUE)
    # add_date= models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title + ' by ' + self.author 


