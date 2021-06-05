from django.urls import path
from . import views

urlpatterns = [
    path('load_category', views.load_category),
    path('restaurant', views.load_category),
    path('wholesaler', views.load_order),
    path('logout', views.logout)
]
