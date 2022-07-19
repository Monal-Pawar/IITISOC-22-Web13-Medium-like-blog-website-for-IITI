from django.urls import path
from . import views
urlpatterns = [
 
  path('contactus',views.contactus),
  path('login',views.login),
  

]