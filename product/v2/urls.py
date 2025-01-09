from django.urls import path
from product.v2.views import ProductListView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
]