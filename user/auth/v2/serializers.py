from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from user.models import User
from django.db.models import Q
from django.contrib.auth.hashers import check_password

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True
    )

    class Meta:
        model = User
        fields = (
            'email', 'phone', 
            'first_name', 'last_name', 
            'password', 'confirm_password'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['email'],  # Using email as username
            **validated_data
        )
        return user

class LoginSerializer(serializers.Serializer):
    login_field = serializers.CharField()  # This will accept either email or phone
    password = serializers.CharField()

class ForgotPasswordSerializer(serializers.Serializer):
    login_field = serializers.CharField()  # Accepts either email or phone
    old_password = serializers.CharField()
    new_password = serializers.CharField(validators=[validate_password])
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        # Check if new_password and confirm_password match
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "confirm_password": "Password fields didn't match."
            })

        # Verify the old password matches the user's current password
        login_field = attrs.get('login_field')
        old_password = attrs.get('old_password')

        # Fetch the user
        user = User.objects.filter(Q(email=login_field) | Q(phone=login_field)).first()
        if not user:
            raise serializers.ValidationError({"login_field": "User not found."})

        if not check_password(old_password, user.password):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})

        # Attach the user object for use in the view
        attrs['user'] = user
        return attrs
