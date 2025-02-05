from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('product/', include('product.v2.urls')),
    path('category/', include('category.v2.urls')),
    path('payment/', include('payment.v2.urls')),
    path('order/', include('order_details.v2.urls')),
    path('cart/', include('cart.v2.urls')), 
    path('user/', include('user.v2.urls')), 
    path('auth/', include('user.auth.v2.urls')), 
    path('shipping/', include('shipping.v2.urls')), 
    path('wishlist/', include('wishlist.v2.urls')),
    path('coupon/', include('coupon.v2.urls')),
]
