from users_app import models
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def load_category(request):
    return render(request, 'category.html')


def get_products(user_id):
    return models.get_products(user_id)

def load_wholesaler_edit(requset):
    context = {
        "products":get_products(requset.session['user_id']),
    }
    return render(requset, 'wholesaler_edit.html', context)


def get_all_meats():
    return models.get_all_meats()

def load_meat(request):
    context = {
        "users": get_all_meats()
    }
    return render(request, 'meat.html', context)

def get_products_for_restauants(user_id):
    return models.get_products_for_restauants(user_id)

def load_order(requset):
    context = {
        'products' : get_products_for_restauants(requset.session['user_id'])
    }
    return render(requset, 'order.html', context)


def set_product(user_id, type, price):
    models.set_product(user_id, type, price)

def add_new_type(request):
    if request.method == 'POST':
        type = request.POST['type']
        price = request.POST['price']
        set_product(request.session['user_id'], type, price)
    return redirect('/wholesaler')



def edit_product(user_id, type, price):
    models.edit_product(user_id, type, price)
    
def edit_product(request):
    if request.method == 'POST':
        type = request.POST['type']
        price = request.POST['price']
        edit_product(request.session['user_id'], type, price)
    return redirect('/wholesaler')

def logout(request):
    request.session.clear()
    return redirect('/')