from rest_framework import serializers
from order_details import Order, OrderDetails


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user', 'order_number',
            'product', 'quantity',
            'order_at', 'total_payment',
            'status', 'tracking_number',
            'estimated_delivery'
        ]
        
class OrderDetailsSerializers(serilaizers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = [
            'order', 'payment_id',
            'transaction_id', 'total_amount',
            'created_at', 'updated_at',
            'status', 'notes',
            'gift_wrap', 'gift_message'
        ]