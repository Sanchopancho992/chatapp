from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='host', null=True)
  description = models.TextField(null=True, blank=True)
  name = models.CharField(max_length=255)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name

class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  message = models.TextField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.message[0:50]
