from rest_framework import generics
from cart.v2.serializers import CartSerializer
from cart.models import Cart

# GET request - List all Carts
class CartListView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# POST request - Create a new Cart
class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer