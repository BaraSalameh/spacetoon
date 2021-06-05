from django.urls import path
from . import views

urlpatterns = [
    path('load_category', views.load_category),
]
