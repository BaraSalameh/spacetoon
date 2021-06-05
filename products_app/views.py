from django.shortcuts import render

# Create your views here.
def load_category(request):
    return render(request, 'category.html')