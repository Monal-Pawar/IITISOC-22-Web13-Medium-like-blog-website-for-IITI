from django.urls import path
from . import views
urlpatterns = [
 
  path('contactus',views.contactus),
  path('createblog',views.createblog),
  path('addblog',views.addblog),
  path('login',views.login),
  path('search',views.search),
  path('category/<str:s>',views.category),


]