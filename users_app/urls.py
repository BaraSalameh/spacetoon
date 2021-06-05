from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.load_login),
    path('load_registration', views.load_registration),
]
   