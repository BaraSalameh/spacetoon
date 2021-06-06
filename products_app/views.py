from django.shortcuts import redirect, render

# Create your views here.
def load_category(request):
    return render(request, 'category.html')

def load_wholesaler_edit(requset):
    return render(requset, 'wholesaler_edit.html')

def load_meat(request):
    return render(request, 'meat.html')

def load_order(requset):
    return render(requset, 'order.html')

def logout(request):
    request.session.clear()
    return redirect('/')