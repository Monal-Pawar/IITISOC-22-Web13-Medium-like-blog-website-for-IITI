from django.shortcuts import render

from blogs.models import Category, Post

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
def login(request):
    return render(request,'blogs/login.html')


  
