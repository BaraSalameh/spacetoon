from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return redirect('/home')

def home(request):
    return render(request, 'home_page.html')

def load_login(request):
    return render(request, 'login.html')