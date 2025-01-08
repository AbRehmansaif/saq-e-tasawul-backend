from rest_framework import serializers
from product.models import Product 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category', 'product_name',
            'description', 'quantity',
            'status', 'coupon',
            'created_at', 'updated_at',
            'trend', 'rate',
            'max_price', 'selling_price',
            'base_price', 'rating',
            'comments', 'sku',
            'brand', 'weight',
            'dimensions', 'meta_title',
            'meta_description', 'slug',
            'tags', 'features',
            'view_count', 'purchase_count'
        ]