from django.urls import path
from payment.v2.views import PaymentView

urlpatterns = [
    path('', PaymentView, name='PaymentView'),
]
