from rest_framework import generics
from wishlist.v2.serializers import WishlistSerializer
from wishlist.models import Wishlist

# GET request - List all Carts
class WishlistSerializerListView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


# POST request - Create a new Cart
class WishlistSerializerCreateView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer