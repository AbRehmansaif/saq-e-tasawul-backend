from rest_framework import serializers
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'order', 'amount',
            'status', 'payment_method',
            'transaction_id', 'payment_date'
        ]