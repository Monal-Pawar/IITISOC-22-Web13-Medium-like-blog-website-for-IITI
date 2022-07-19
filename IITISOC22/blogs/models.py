from turtle import title
from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField 
# Create your models here.

#Category model

class Category(models.Model):
    # only title need to be written here
    cat_id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    description= models.TextField()
    url= models.CharField(max_length=100)
    # image??
    author= models.CharField(max_length=100)
    add_date= models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
    

#Post model
class Post(models.Model):
    post_id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    # discription for first 100 words excluding img
    content= HTMLField()
    url= models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

