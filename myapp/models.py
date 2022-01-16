from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model) :
    content = models.CharField(max_length=10000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    # sender = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return str(self.id)

class Group(models.Model) :
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name