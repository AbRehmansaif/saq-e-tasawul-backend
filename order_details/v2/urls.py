from django.urls import path
from order_details.v2.views import OrderView, OrderDetailsView

urlpatterns = [
    path('', OrderView, name='OrderView'),
    path('details/', OrderDetailsView, name='OrderDetailsView'),
]
