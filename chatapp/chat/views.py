from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .models import Room, Message
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serializers import RoomSerializer, MessageSerializer
from django.urls import reverse_lazy


class HomeView(TemplateView):
  template_name = 'index.html'
  serializer_class = RoomSerializer
  
  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    q = self.request.GET.get('q', '')
    rooms = Room.objects.filter(
      Q(name__icontains=q) |
      Q(description__icontains=q) 
    )
    
    room_count = rooms.count()
    room_message = Message.objects.filter(
      Q(room__name__icontains=q)
    )
    
    context['rooms'] = rooms
    context['room_count'] = room_count
    context['room_message'] = room_message
    return context
  
  
class LoginView(FormView):
  template_name = 'login.html'
  form_class = LoginForm
  success_url = '/chat/'
  
  def form_valid(self, form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(self.request,username=username, password=password)
    
    if user is not None:
      login(self.request, user)
      return super().form_valid(form)
    else:
      messages.error(self.request, 'Invalid username or password')
      return self.form_invalid(form)
    
  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    context['form'] = LoginForm()
    return context
  
  def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
    context =  super().dispatch(request, *args, **kwargs)
    if self.request.user.is_authenticated:
      return redirect('home')
    return context


class RoomView(TemplateView):
  template_name = 'room.html'
  
  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    room_name = self.kwargs['pk']
    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=room)
    context['room'] = room
    context['messages'] = messages
    return context
 
class LogoutView(TemplateView):
  def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
    logout(request)
    return redirect('home')
  
  
class RegisterView(TemplateView):
  template_name = 'register.html'
  