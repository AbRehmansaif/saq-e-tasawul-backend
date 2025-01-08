from rest_framework import serializers
from sub_category.models import SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'category', 'name',
            'description', 'created_at',
            'updated_at', 'image',
            'is_active', 'meta_title', 
            'meta_description', 'slug'
        ]