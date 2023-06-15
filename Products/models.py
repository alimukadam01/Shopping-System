from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator

# Create your models here.
class ProductCategory(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.category) + ": " + str(self.subcategory)
 

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'reviews')
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

