#apps/my_app/views.py

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
import random

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime



def index(request):
    #--- Homepage
    return redirect('/login')
    
    
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(response, 'my_app/index.html', {"form":form})

def profile(request):
    return render(request, 'my_app/profile.html')