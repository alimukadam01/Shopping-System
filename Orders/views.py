from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from Customers.models import Customer
from .models import Order
from .serializers import createOrderSerializer, orderSerializer, updateOrderSerializer

# Create your views here.

class orderViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = createOrderSerializer(
                        data=request.data,
                        context = {'user_id': self.request.user.id}
                    )   
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = orderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return createOrderSerializer
        elif self.request.method == 'PATCH':
            return updateOrderSerializer
        return orderSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()
        
        customer = Customer.objects.get(user_id = user.id)
        return Order.objects.filter(customer = customer)