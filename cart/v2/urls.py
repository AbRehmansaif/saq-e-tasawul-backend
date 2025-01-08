from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.v2.views import CartViewSet


router = DefaultRouter()
router.register('cart-entry'', CartViewSet, basename='cart-entry')

urlpatterns = [
    path('', include(router.urls)),
]
