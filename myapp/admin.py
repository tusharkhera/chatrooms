from operator import mod
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin) :
    list_display = ['id', 'content', 'timestamp', 'group', 'sender']

@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin) :
    list_display = ['id', 'name']