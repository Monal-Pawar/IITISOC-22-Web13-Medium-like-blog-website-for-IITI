from turtle import title
from django.shortcuts import render

from blogs.models import Category, Post
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import path
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from django.contrib import messages
from django.contrib import messages
import datetime
import os

#home
def home(request):
    # load all the posts from db(10)
    post = Post.objects.all()
    # load all the category from db(10)
    
    # print(post)
    cats = Category.objects.all()
    data={
        'post':post,
        'cats':cats,
    }
    print(post,cats)

    return render(request,'blogs/home.html',data)


#contactus
def contactus(request):
    return render(request,'blogs/contactus.html')

#login
def createblog(request):
    # post = Post.objects.all().order_by('sno')
    cats = Category.objects.all()
    data={
        'cats':cats
    }
    return render(request,'blogs/create.html',data)
    
    
#login
def login(request):
    return render(request,'blogs/login.html')

#addblog
def addblog(request):
    if request.method == "POST":
        title = request.POST.get('Addblogt')
        content = request.POST.get('Addblogc')
        descr = request.POST.get('Addblogd')
        author = 'monal'
        cat = request.POST.get('drop')
        
        addblogtotal= Post(title=title,description=descr,content=content,cat=cat)
        addblogtotal.save()

        messages.success(request,"Blog added successfully!")
        
        print(content,cat)
        return redirect('/')

def search(request):
    querysearch=request.GET['querysearch']
    post = Post.objects.filter(title__icontains=querysearch)
    cats = Category.objects.all()
    data={
        'post':post,
        'cats':cats,
    }
    print(post,cats)

    return render(request,'blogs/home.html',data)

def category(request,s):
    post = Post.objects.filter(cat__icontains=s)
    cats = Category.objects.all()
    data={
        'post':post,
        'cats':cats,
    }
    print(post,cats)
    return render(request,'blogs/home.html',data)

  
