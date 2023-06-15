"""ShoppingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Customers import views as customerViews
from Products import views as productViews
from Orders import views as orderViews 
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', productViews.productViewSet, basename='product')
router.register('carts', productViews.cartViewSet)
router.register('customers', customerViews.customerViewSet)
router.register('orders', orderViews.orderViewSet, basename='orders')
router.register('categories', productViews.categoryViewSet)


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', productViews.reviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', productViews.cartItemViewSet, basename='cart-items')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
    path(r'', include(carts_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('customers/', customerViews.get_or_create_address.as_view()),
    path('customer-addresses/', customerViews.get_or_create_address.as_view()),
]