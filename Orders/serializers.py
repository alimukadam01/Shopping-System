from django.db import transaction
from rest_framework import serializers
from Customers.models import Customer
from Customers.signals import order_created
from Products.models import Cart, CartItem
from Products.serailizers import simpleProductSerializer
from .models import Order, OrderItem, Payment, PaymentMethod


class orderItemSerializer(serializers.ModelSerializer):
    product = simpleProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity']
        
class orderSerializer(serializers.ModelSerializer):
    items = orderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'placed_at', 'customer', 'payment', 'timings', 'promocode', 'discount', 'items']

class createOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart with the given id was found.')
        if CartItem.objects.filter(cart = cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty.')
        return cart_id

    def save(self, **kwargs):
        with transaction.atomic():
            cart = self.validated_data['cart_id']

            customer = Customer.objects.get(user = self.context['user_id'])
            order = Order.objects.create(customer = customer)

            cartitems = CartItem.objects.select_related('product').filter(cart = cart)
            orderitems = [
                OrderItem(
                    order = order,
                    product = item.product,
                    price = item.product.price,
                    quantity = item.quantity
                ) for item in cartitems
            ]
            OrderItem.objects.bulk_create(orderitems)

            Cart.objects.filter(pk=cart).delete()

            order_created.send_robust(self.__class__, order=order)
            return order

class updateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment']

class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = []


class paymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = []


