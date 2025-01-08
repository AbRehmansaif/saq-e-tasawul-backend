from rest_framework import serializers
from coupon.models import Coupon


class CouponSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'product', 'coupon',
            'quantity', 'discount_type',
            'discount_value', 'valid_from',
            'valid_to', 'minimum_purchase', 
            'is_active', 'usage_limit',
            'times_used'
        ]