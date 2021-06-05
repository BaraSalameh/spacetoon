from django.shortcuts import redirect, render
from . import models


# Create your views here.

def index(request):
    return redirect('/home')

def home(request):
    return render(request, 'home.html')

def load_login(request):
    return render(request, 'login.html')

def load_registration(request):
    return render(request, 'Registration.html')
