from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsAdminOrReadOnly
from .models import Cart, CartItem, Product, ProductCategory, Review
from .serailizers import addCartItemSerializer, cartItemSerializer, cartSerializer, categorySerializer, productSerializer, reviewSerializer, updateCartItemSerializer
from .filters import ProductFilter
# Create your views here.
class categoryViewSet(ModelViewSet, GenericViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = categorySerializer


class productViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAdminOrReadOnly,]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'quantity']

    def get_serializer_context(self):
        return {'request': self.request}


class reviewViewSet(ModelViewSet):
    serializer_class = reviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    
    
class cartViewSet(CreateModelMixin, 
                    RetrieveModelMixin, 
                    GenericViewSet, 
                    DestroyModelMixin):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = cartSerializer


class cartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete',]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return addCartItemSerializer
        elif self.request.method == 'PATCH':
            return updateCartItemSerializer
        return cartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')