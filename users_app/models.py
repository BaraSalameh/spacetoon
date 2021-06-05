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
    logo = models.CharField(max_length=255, default="https://www.pngkey.com/png/detail/62-627900_white-question-mark-on-a-black-circular-background.png")
    phone_number=models.CharField(max_length=255, default=True)
    category_id = models.ForeignKey(UserCategory, related_name='wholesalers', on_delete=CASCADE, null=True)
    address_id = models.OneToOneField(Address, on_delete=CASCADE)
    role_id = models.ForeignKey(Role, related_name= 'type', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def address_crate(city,street,building_number):
    Address.objects.create(city=city,street=street,building_number=building_number)
    address = Address.objects.last()
    return address

def get_role(role):
    role = Role.objects.filter(name = role)
    return role[0]

def create_user(name,email,password,logo,phone_number,category_id ,city, street, building_number, role):
    category = get_category(category_id)
    roles = get_role(role)
    address = address_crate(city, street, building_number)
    return User.objects.create(name=name, email=email, password=password, logo=logo, phone_number=phone_number,category_id = category,address_id= address, role = roles)




def get_category(name):
    category = UserCategory.objects.filter(name = name)
    return category[0]

def get_user(email,password):
    users=User.objects.filter(email = email, password = password)
    if len(users) > 0 :
        return users[0]
    return None
