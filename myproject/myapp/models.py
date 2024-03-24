from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    mobile=models.CharField(max_length=15)
    address=models.CharField(max_length=255)


class Student(models.Model):
    name=models.CharField(max_length=255)
    email_id=models.CharField(max_length=255)
    city=models.CharField(max_length=50)

class Category(models.Model):
    cat_name=models.CharField(max_length=200)
    cat_desc=models.CharField(max_length=255)
    
    def __str__(self):
        return self.cat_name

class Item(models.Model):
    i_name=models.CharField(max_length=255)
    i_price=models.CharField(max_length=20)
    i_desc=models.CharField(max_length=255)
    i_imgage=models.ImageField(upload_to='item_image/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.i_name