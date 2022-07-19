from django.shortcuts import render

from blogs.models import Category, Post
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import path
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from django.contrib import messages
import datetime
import os

#home
def home(request):
    # load all the posts from db(10)
    post = Post.objects.all()[:11]
    # load all the category from db(10)
    cats = Category.objects.all()
    # print(post)
    data={
        'post':post,
        'cats':cats
    }

    return render(request,'blogs/home.html',data)


#contactus
def contactus(request):
    return render(request,'blogs/contactus.html')

#login
def createblog(request):
    return render(request,'blogs/create.html')
    
    
#login
def login(request):
    return render(request,'blogs/login.html')


def addblog(request):
    if request.method == "POST":
        title = request.POST.get('Addblogt')
        content = request.POST.get('Addblogc')
        print(content)
        return HttpResponse("hello monal bai how r u")


  
