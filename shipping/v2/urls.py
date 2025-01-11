from django.urls import path
from shipping.v2.views import ShippingDetailsListView, ShippingDetailsCreateView

urlpatterns = [
    path('', ShippingDetailsListView.as_view(), name='cart-list'),
    path('create/', ShippingDetailsCreateView.as_view(), name='cart-create'),
]