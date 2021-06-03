from django.urls import path
from . import views

urlpatterns = [
    path('category' ,views.wholesalerType)   # method for wholesalerType for wholesaler
]
