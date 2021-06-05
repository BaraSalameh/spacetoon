from django.shortcuts import redirect, render

# Create your views here.
def load_category(request):
    return render(request, 'category.html')

def load_order(requset):
    return render(requset, 'order.html')

def logout(request):
    request.session.clear()
    return redirect('/')