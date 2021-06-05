from django.shortcuts import redirect, render
from django.contrib import messages
from users_app import models

# Create your views here.

def index(request):
    return redirect('/home')

def home(request):
    return render(request, 'home.html')

def load_login(request):
    return render(request, 'login.html')

def load_registration(request):
    return render(request, 'Registration.html')

def createuser(name,email,password,logo,phone_number,category_id ,city, street, building_number, role):
    return models.create_user

def validate_registration(name,email,password,logo,phone_number,category_id ,city, street, building_number, role):
    return models.validate_registration(name,email,password,logo,phone_number,category_id ,city, street, building_number, role)

def registration(request):
    if request.method == 'POST':   
        name=request.POST['client_name']
        email=request.POST['email']
        password=request.POST['password'] 
        confirm_password=request.POST['confirm_password']
        logo = request.POST['logo']
        phone_number = request.POST['phone_number']
        city = request.POST['city']
        street = request.POST['street']
        building_number = request.POST['building_number']
        category_id= request.POST['client_category']
        role= request.POST['client_type']
        errors = validate_registration(name,email,password,logo,phone_number,category_id ,city, street, building_number, role)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/load_registration')
        user = createuser(name,email,password,logo,phone_number,category_id ,city, street, building_number, role)
        request.session['id'] = user.id
        request.session['name'] = user.name
        if role == 'Restaurant':
            return redirect('/restaurant')
        if role == 'Wholesaler': 
            return redirect('/wholesaler')
    return redirect('/load_registration')
    

def whole(request):
    return render(request,'WholesalersEdit.html')