from rest_framework import generics
from product.v2.serializers import ProductSerializer
from product.models import Product

# GET request - List all products
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# POST request - Create a new product
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer