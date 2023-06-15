from django.contrib import admin
from .models import Product, ProductCategory, Review, Cart, CartItem

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)