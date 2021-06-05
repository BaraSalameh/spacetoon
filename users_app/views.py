from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return redirect('/home')

def home(request):
    return render(request, 'home.html')

def load_login(request):
    return render(request, 'login.html')

def load_registration(request):
    return render(request, 'Registration.html')

def validate_login(email, password):
    """
    Description: Function to validate the login values
    parametres: email -> the user email from login form
                password -> the user password from login form
    Return: dictionary of errors if there any
    """
    return models.validate_login(email, password)

def confirm_login(email, password):
    """
    Description: Function to confirm the login values(if this user exists)
    parametres: email -> the user email from login form
                password -> the user password from login form
    Return: the role_id id to check if the user is a restaurant or wholesaler
    """
    return models.confirm_login(email, password)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        login_validation = validate_login(email, password)
        if len(login_validation) > 0:
            for key, value in login_validation.items():
                messages.error(request, value)
            return redirect('/load_login')
        login_confirm = confirm_login(email, password)
        if login_confirm == 1:
            pass
        if login_confirm == 2:
            return redirect('/load_category')
    return redirect('/load_login')
