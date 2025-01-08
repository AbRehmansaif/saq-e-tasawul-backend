from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 'description',
            'imange', 'is_active',
            'meta_title', 'meta_description',
            'slug', 'created_at',
            'updated_at'
        ]