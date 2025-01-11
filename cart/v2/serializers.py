from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'user', 'total_products',
            'products', 'created_at',
            'updated_at', 'session_id',
            'total_amount'
        ]