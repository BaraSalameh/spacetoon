from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
# Create your views here.

def index(request):
    return redirect('/home')


def get_all_wholesalers():
    return models.get_all_wholesalers()

def get_all_restaurants():
    return models.get_all_restaurants()

def home(request):
    context = {
        'wholesalers': get_all_wholesalers(),
        'restaurants': get_all_restaurants(),
    }
    return render(request, 'home.html', context)

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
        password = request.POST['passwords']
        login_validation = validate_login(email, password)
        if len(login_validation) > 0:
            for key, value in login_validation.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/login')
        login_confirm = confirm_login(email, password)
        if login_confirm == 1:
            return redirect('/wholesaler')
        if login_confirm == 2:
            return redirect('/load_category')
    return redirect('/login')
    
def createuser(name, email, password, logo, phone_number,role, category_id,city, street, building_number):
    return models.create_user(name, email, password, logo, phone_number,role, category_id,city, street, building_number)

def validate_registration(name, email, password, confirm_password, logo, phone_number, city, street, building_number):
    return models.validate_registration(name, email, password, confirm_password, logo, phone_number, city, street, building_number)

def registration(request):
    if request.method == 'POST':   
        name=request.POST['client_name']
        email=request.POST['email']
        password=request.POST['passwords'] 
        confirm_password=request.POST['confirm_password']
        logo = request.POST['logo']
        if len(logo) < 1:
            logo = "https://www.pngkey.com/png/detail/62-627900_white-question-mark-on-a-black-circular-background.png"
        phone_number = request.POST['phone_number']
        city = request.POST['city']
        street = request.POST['street']
        building_number = request.POST['building_number']
        if request.POST['client_category'] != '7':
            role = 1
        if request.POST['client_category'] == '7':
            role = 2
        print(request.POST['client_category'])
        print(role)
        category_id= request.POST['client_category']
        errors = validate_registration(name, email, password, confirm_password, logo, phone_number, city, street, building_number)
        print(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/load_registration')
        print("there is no errors")
        user = createuser(name, email, password, logo, phone_number, role, category_id, city, street, building_number)
        print("every thing is okay")
        request.session['id'] = user.id
        request.session['name'] = user.name
        if role == 2:
            return redirect('/restaurant')
        if role == 1: 
            return redirect('/wholesaler')
    return redirect('/load_registration')
    

def whole(request):
    return render(request,'WholesalersEdit.html')

