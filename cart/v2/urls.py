from django.urls import path
from cart.v2.views import CartListView, CartCreateView

urlpatterns = [
    path('', CartListView.as_view(), name='cart-list'),
    path('create/', CartCreateView.as_view(), name='cart-create'),
]