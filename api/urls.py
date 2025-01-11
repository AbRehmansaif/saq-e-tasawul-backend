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
]
