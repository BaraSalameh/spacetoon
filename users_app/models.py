from django.db import models
from django.db.models.deletion import CASCADE


class Role(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserCategory(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role_id = models.ForeignKey(Role, related_name= 'type', on_delete=CASCADE)
    address_id = models.OneToOneField(Address, on_delete=CASCADE)
    category_id = models.ForeignKey(UserCategory, related_name='wholesalers', on_delete=CASCADE, null=True)
    logo = models.CharField(max_length=255, default="https://www.pngkey.com/png/detail/62-627900_white-question-mark-on-a-black-circular-background.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)