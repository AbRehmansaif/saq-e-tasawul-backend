from django.urls import path
from coupon.v2.views import CouponSerializerListView, CouponSerializerCreateView

urlpatterns = [
    path('', CouponSerializerListView.as_view(), name='cart-list'),
    path('create/', CouponSerializerCreateView.as_view(), name='cart-create'),
]