from turtle import title
from django.contrib import admin
from .models import Category,Post
# Register your models here.

#for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('title',)
    search_fields= ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display= ('title','content')
    search_fields= ('title',)
    list_filter= ('cat',)
    # list_per_page: 10


admin.site.register(Category,CategoryAdmin) 
admin.site.register(Post,PostAdmin)

