from django.db import models
from django.contrib.auth.models import User #Users from Django 
# Create your models here.

#Class for Topic
class Topic(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self): return self.name
    
#Room Model
class Room(models.Model):
    host =  models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length=200) #Allows different names
    description = models.TextField(null = True, blank = True) #Blank page for decription 
    #participants = 
    updated = models.DateTimeField(auto_now = True) # Shows time 
    created = models.DateTimeField(auto_now_add = True) #shows time of creation  

    def __str__(self):
        return self.name
    
#Models that outputs a message 
class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) #A for Users relationship with Room class that deletes all the childern
    room = models.ForeignKey(Room, on_delete = models.CASCADE) #A for room relationship with Room class that deletes all the childern
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True) # Shows time 
    created = models.DateTimeField(auto_now_add = True) #shows time of creation  

    def __str__(self):
        return self.body[0:50]
