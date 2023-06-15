from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100 , null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.address)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    addresses = models.ManyToManyField(Address, through='CustomerAddress', blank=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        permissions = [
            ('view_history', 'Can view history'),
        ]


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    territory = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.customer) + ': ' + str(self.territory)

    class Meta:
        unique_together = [('customer', 'address'),]

