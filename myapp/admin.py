from operator import mod
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin) :
    list_display = ['id', 'content', 'timestamp', 'group', 'sender']
    list_filter = ['sender', 'group']
    list_per_page = 20
    search_fields = ('content',)

@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin) :
    list_display = ['id', 'name', 'unique_id', 'admin']
    list_filter = ['name', 'admin']
    list_per_page = 20
    search_fields = ('name', 'unique_id', 'admin',)

@admin.register(ChatList)
class ChatListModelAdmin(admin.ModelAdmin) :
    list_display = ['id', 'chat_user', 'grp']
    list_filter = ['chat_user', 'grp']
    list_per_page = 20
    search_fields = ('chat_user', 'grp',)

