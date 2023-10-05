from django.db import models
from datetime import datetime,date
from django.db.models.fields import (DateTimeField,DurationField,DateField,TimeField)

# Create your models here.
class AdminDetailsModel(models.Model):
    admin_name=models.CharField(max_length=200)
    admin_mobile=models.CharField(max_length=200)
    admin_email=models.CharField(max_length=200)
    admin_password=models.CharField(max_length=200)
class RegisterUserModel(models.Model):
    user_name=models.CharField(max_length=200)
    user_mobile=models.CharField(max_length=200)
    user_email=models.CharField(max_length=200)
    user_password=models.CharField(max_length=200)
    user_image=models.ImageField(upload_to='static/user_images')

class AuctionModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(upload_to='static/',null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    

class userBidModel(models.Model):
    user_name = models.CharField(max_length=200)
    user_amount = models.DecimalField(max_digits=10, decimal_places=2)
    