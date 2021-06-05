from typing import Optional
from django.db import models
from django.db.models.deletion import CASCADE
import bcrypt
import re

class BlogManager(models.Manager):
    def basic_validator(self, postData ):
        errors = {}
        LOGO_REGEX = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
        if not LOGO_REGEX.match(postData['logo']):
            errors['logo'] = "Invalid logo path!"


        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(postData['Email']):    
            errors['Email'] = "Invalid email address!"
        if len(postData['client_name']) < 2:
            errors["client_name"] = "client name should be at least 2 characters"
        if len(postData['phone_number']) < 7:
            errors["phone_number"] = "phone number should be at least 7 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "your password should be at least 8 characters"
        if len(postData['city']) < 2:
            errors["city"] = "your city should be at least 2 characters"
        if len(postData['street']) < 2:
            errors["street"] = "your city should be at least 2 characters"
        if len(postData['building_number']) < 1:
            errors["building_number"] = "your building_number should be at least 1 characters"
        

       
        return errors

        
    def validate_login(self, email , password):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(email['Email']):    
            errors['Email'] = "Invalid email address!"
        if len(password['password']) < 8:
            errors["password"] = "your password should be at least 8 characters"
        return errors
        
    

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
    logo = models.CharField(max_length=255, default="https://www.pngkey.com/png/detail/62-627900_white-question-mark-on-a-black-circular-background.png")
    category_id = models.ForeignKey(UserCategory, related_name='wholesalers', on_delete=CASCADE, null=True)
    address_id = models.OneToOneField(Address, on_delete=CASCADE)
    role_id = models.ForeignKey(Role, related_name= 'type', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)