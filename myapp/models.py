from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null

# Create your models here.
class Chat(models.Model) :
    content = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return str(self.id)

class Group(models.Model) :
    name = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=50, default='', blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self) :
        return self.unique_id

class ChatList(models.Model) :
    chat_user = models.ForeignKey(User, on_delete=models.CASCADE)
    grp = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, default='')


    