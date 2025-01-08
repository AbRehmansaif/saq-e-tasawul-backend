from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from cart.models import Cart


class CartSerializer(serializer):
    class Meta:
        model = Cart
        fields = [
            'user', 'total_products',
            'products', 'created_at',
            'updated_at', 'serrion_id',
            'total_amount'
        ]