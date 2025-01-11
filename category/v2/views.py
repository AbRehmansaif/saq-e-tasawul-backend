from rest_framework import generics
from category.v2.serializers import CategorySerializer
from category.models import Category


# GET request - List all products
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# POST request - Create a new product
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer