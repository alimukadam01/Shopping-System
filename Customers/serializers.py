from rest_framework import serializers
from .models import Address, Customer, CustomerAddress

class addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'city', 'phone', 'description']


class customerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    addresses = addressSerializer(many=True)

    class Meta:
        model = Customer
        fields = ['user_id', 'phone', 'addresses',]


class customerAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAddress
        fields = ['customer', 'address']


