from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.load_login),
    path('registration', views.load_registration),
    path('real_login', views.login),
]
