from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.load_login),
<<<<<<< HEAD
    path('registration', views.load_registration),
    path('real_login', views.login),
=======
    path('load_registration', views.load_registration),
    path('whole',views.whole),
>>>>>>> e51cec675657e661c5aab2efbfabdeeac17be158
]
