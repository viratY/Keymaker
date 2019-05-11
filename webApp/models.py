from django.db import models
from phone_field.models import PhoneField

# Create your models here.

class Customer(models.Model):

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phoneNumber =  PhoneField(blank=False, null=False, unique=True, help_text='Contact phone number')

class KeyMaker(models.Model):

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phoneNumber = PhoneField(blank=False, null=False, unique=True, help_text='Contact phone number')

class Request(models.Model):

    # location = models.PointField()
    location = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,related_name='CustomerRequests',on_delete=models.CASCADE)
    keymaker = models.ForeignKey(KeyMaker,related_name='KeymakerRequests',on_delete=models.CASCADE)

class Charges(models.Model):

    requestId = models.ForeignKey(Request,related_name='Charges',on_delete=models.CASCADE)
    charge = models.IntegerField(null=False,blank=False)
    paid = models.BooleanField()

