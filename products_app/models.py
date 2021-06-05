from django.db import models
from django.db.models.deletion import CASCADE
from users_app.models import User

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category_id = models.ForeignKey(ProductCategory, related_name='category_products', on_delete=CASCADE)
    order = models.ManyToManyField(User, related_name='user_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

