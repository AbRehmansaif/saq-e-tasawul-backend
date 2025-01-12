from rest_framework import generics
from coupon.v2.serializers import CouponSerializer
from coupon.models import Coupon

# GET request - List all Carts
class CouponSerializerListView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


# POST request - Create a new Cart
class CouponSerializerCreateView(generics.CreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer