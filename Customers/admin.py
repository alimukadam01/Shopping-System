from django.contrib import admin
from .models import Customer, Address, CustomerAddress
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(Address)