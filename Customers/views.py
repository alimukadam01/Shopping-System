from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from Customers.models import Customer, CustomerAddress, Address
from Customers.permissions import FullDjangoModelPermissions, ViewCustomerHistoryPermission
from .serializers import customerSerializer, customerAddressSerializer, addressSerializer

# Create your views here.
class customerViewSet(ModelViewSet):
    
    queryset = Customer.objects.all()
    serializer_class = customerSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response('ok')
         
    @action(detail = False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.get(user_id = request.user.id)
        if request.method == 'GET':
            return Response(customerSerializer(customer).data)
        elif request.method == 'PUT':
            serializer = customerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class get_or_create_address(APIView):
    def get(self, request):
        return Response(addressSerializer(Address.objects.all(), many = True).data)

    def post(self, request):
        address = addressSerializer(request.data)
        address.is_valid(raise_exception=True)
        return Response(address)


class get_or_create_customerAddress(APIView):
    def get(self, request):
        return Response(customerAddressSerializer(CustomerAddress.objects.all(), many = True).data)

    def post(self, request):
        customerAddress = customerAddressSerializer(request.data)
        customerAddress.is_valid(raise_exception=True)
        return Response(customerAddress)