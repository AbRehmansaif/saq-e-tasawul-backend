from rest_framework import generics
from shipping.v2.serializers import ShippingDetailsSerializer
from shipping.models import ShippingDetails

# GET request - List all Carts
class ShippingDetailsListView(generics.ListCreateAPIView):
    queryset = ShippingDetails.objects.all()
    serializer_class = ShippingDetailsSerializer


# POST request - Create a new Cart
class ShippingDetailsCreateView(generics.CreateAPIView):
    queryset = ShippingDetails.objects.all()
    serializer_class = ShippingDetailsSerializer