from users_app import models
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def load_category(request):
    return render(request, 'category.html')

def load_wholesaler_edit(requset):
    return render(requset, 'wholesaler_edit.html')


def get_all_meats():
    return models.get_all_meats()

def load_meat(request):
    context = {
        "users": get_all_meats()
    }
    return render(request, 'meat.html', context)

def load_order(requset):
    return render(requset, 'order.html')

def logout(request):
    request.session.clear()
    return redirect('/')