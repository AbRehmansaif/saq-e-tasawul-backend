from django.urls import path
from wishlist.v2.views import WishlistSerializerListView, WishlistSerializerCreateView

urlpatterns = [
    path('', WishlistSerializerListView.as_view(), name='cart-list'),
    path('create/', WishlistSerializerCreateView.as_view(), name='cart-create'),
]