from typing import Optional
from django.contrib.messages.api import error
from django.db import models
from django.db.models.deletion import CASCADE
import bcrypt
import re

class UserManager(models.Manager):
    def basic_validator(self, name, email, password, confirm_password, logo, phone_number, city, street, building_number):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        LOGO_REGEX = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
        if not LOGO_REGEX.match(logo):
            errors['logo'] = "Invalid logo path!"
        if not EMAIL_REGEX.match(email):    
            errors['email'] = "Invalid email address!"
        if len(name) < 2:
            errors["client_name"] = "client name should be at least 2 characters"
        if len(phone_number) < 7:
            errors["phone_number"] = "phone number should be 7 digits at least"
        if len(password) < 8:
            errors["password"] = "your password should be at least 8 characters"
        if len(confirm_password) < 8 and confirm_password != password:
            error['confirm_password'] = "Your confirmation password should equals the password"
        if len(city) < 2:
            errors["city"] = "your city should be at least 2 characters"
        if len(street) < 2:
            errors["street"] = "your city should be at least 2 characters"
        if len(building_number) < 1:
            errors["building_number"] = "your building_number should be at least 1 characters"
        return errors
        
    def login_validate(self, email , password):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(email):    
            errors['email'] = "Invalid email address!"
        if len(password) < 8:
            errors["password"] = "your password should be at least 8 characters"
        return errors
        
    

class Role(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.city


class UserCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, default="https://www.pngkey.com/png/detail/62-627900_white-question-mark-on-a-black-circular-background.png")
    phone_number=models.CharField(max_length=255, default=True)
    role_id = models.ForeignKey(Role, related_name= 'type', on_delete=CASCADE)
    category_id = models.ForeignKey(UserCategory, related_name='wholesalers', on_delete=CASCADE, null=True)
    address_id = models.OneToOneField(Address, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    objects = UserManager()



def validate_login(email, password):
    return User.objects.login_validate(email, password)

def validate_registration(name, email, password, confirm_password, logo, phone_number, city, street, building_number):
    return User.objects.basic_validator(name, email, password, confirm_password, logo, phone_number, city, street, building_number)

def confirm_login(email, password):
    user = User.objects.filter(email=email, password=password)
    if user:
        return user[0].role_id.id
    return None

def address_crate(city,street,building_number):
    Address.objects.create(city=city,street=street,building_number=building_number)
    address = Address.objects.last()
    return address

def get_role(id):
    role = Role.objects.get(id = id)
    return role

def create_user(name, email, password, logo, phone_number,role, category_id,city, street, building_number):
    category = get_category(category_id)
    roles = get_role(role)
    address = address_crate(city, street, building_number)
    return User.objects.create(name=name, email=email, password=password, logo=logo, phone_number=phone_number,role_id = roles,category_id = category,address_id= address)

def get_category(id):
    category = UserCategory.objects.get(id = id)
    return category

def get_user(email,password):
    users=User.objects.filter(email = email, password = password)
    if len(users) > 0 :
        return users[0]
    return None
