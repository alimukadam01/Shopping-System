from django.db import models
from Customers.models import Customer
from Products.models import Product

# Create your models here.

class PaymentMethod(models.Model):
    pass


class Payment(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = {
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    }

    amount = models.IntegerField(null=True, blank=True)
    method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

class Order(models.Model):
    
    DELIVERY_TIME_CHOICES = {
        ('Morning', '06.00-12.00'),
        ('Evening', '12.00-18.00'),
        ('Night', '18.00-23.00'),
    }

    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order')
    timings = models.CharField(max_length=255, choices=DELIVERY_TIME_CHOICES, null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    promocode = models.CharField(max_length=255, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel order')
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitem')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)