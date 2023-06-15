from rest_framework import serializers
from .models import Cart, CartItem, Product, Review, ProductCategory

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category', 'subcategory']

class productSerializer(serializers.ModelSerializer):
    category = categorySerializer()
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description']

class simpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price',]


class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']
 
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


class cartItemSerializer(serializers.ModelSerializer):
    product = simpleProductSerializer()
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self, cartitem: CartItem):
        return cartitem.quantity * cartitem.product.price

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price',]


class addCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('Product with the provided ID was not found.')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            #Cartitem exists and we need to update
            cart_item = CartItem.objects.get(cart_id = cart_id, product_id = product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            #Cartitem doesn't exist and we need to create one
            self.instance = CartItem.objects.create(cart_id = cart_id, **self.validated_data)
        
        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class updateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity',]


class cartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = cartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self, cart):
       return sum([item.quantity * item.product.price for item in  cart.items.all()])

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price',]