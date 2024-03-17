from rest_framework import serializers
from .models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id', 'name', 'description', 'host', 'created_at', 'updated_at')
    
class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ('id', 'user', 'room', 'message', 'created_at', 'updated_at')
    

