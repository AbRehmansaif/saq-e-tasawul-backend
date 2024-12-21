from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from user.models import User
class UserRegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password_2 = serializers.CharField(
        write_only=True, 
        required=True
    )
    class Meta:
        model = User
        fields = (
            'username', 'email', 
            'first_name', 'last_name', 
            'password_1', 'password_2',
            'is_active', 'created_at',
            'updated_at'
        )
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }
    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError(
                {"password_2": "Password fields didn't match."}
            )
        return attrs
    def create(self, validated_data):
        validated_data.pop('password_2')
        password = validated_data.pop('password_1')
        
        user = User.objects.create_user(
            **validated_data,
            password=password
        )
        return user
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 
            'first_name', 'last_name', 
            
            'is_active', 'created_at',
            'updated_at', 'id'
        )
        read_only_fields = (
            'id', 'user_name', 'email', 
            'is_active', 'created_at'
        )