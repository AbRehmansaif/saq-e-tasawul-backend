from rest_framework import serializers
from shipping.models import ShippingDetails


class ShippingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetails
        fields = [
            'order', 'address_line_1',
            'address_line_2', 'country',
            'city', 'postal_code',
            'phone_number', 'created_at',
            'updated_at', 'shipping_method',
            'tracking_url', 'estimated_delivery',
            'shipping_instructions'
        ]