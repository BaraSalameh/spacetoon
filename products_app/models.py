from django.db import models
from django.db.models.deletion import CASCADE
from users_app.models import *

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category_id = models.ForeignKey(UserCategory, related_name='category_products', on_delete=CASCADE)
    order = models.ManyToManyField(User, related_name='user_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


def get_products_for_restauants(user_id):
    user = User.objects.get(id=19)
    return user.user_products.all()

def edit_product(user_id, type, price):
    pass

def set_product(user_id, type, price):
    user = User.objects.get(id = user_id)
    new_product = Product.objects.create(name = type, price = price , category_id = user.category_id)
    user.user_products.add(new_product)

def get_all_meats():
    return User.objects.filter(category_id = 1)

def get_products(user_id):
    user = User.objects.get(id = user_id)
    return user.user_products.all()
    