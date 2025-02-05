from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from user.models import User
from django.db.models import Q
from django.contrib.auth.hashers import check_password


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 
            'phone', 'first_name', 
            'last_name', 'address', 
            'city', 'country', 
            'postal_code', 'profile_image', 
            'profile_completed'
        )
        read_only_fields = (
            'id', 'email', 
            'phone', 'profile_completed'
        )