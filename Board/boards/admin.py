from django.contrib import admin
from .models import Board,Topic,Post
from django.contrib.auth.models import Group  
# Register your models here.

admin.site.register(Board)
admin.site.register(Topic)
admin.site.unregister(Group)

admin.site.site_header='Boards Admin Panel'
admin.site.site_title ='Boards Admin Panel'