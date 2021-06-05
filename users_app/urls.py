from django.urls import path
from . import views
from products_app import urls

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.load_login),
    path('registration', views.load_registration),
    path('real_login', views.login),
    path('load_registration', views.load_registration),
    path('whole',views.whole),
    path('real_registration', views.registration),
]
