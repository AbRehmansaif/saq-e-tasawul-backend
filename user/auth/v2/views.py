from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.db.models import Q
from user.models import User
from user.auth.v2.serializers import (
    RegistrationSerializer, 
    LoginSerializer, 
    ForgotPasswordSerializer
)
from user.v2.serializers import UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ForgotPasswordSerializer

    def get_permissions(self):
        if self.action in ['register', 'login', 'forgot_password'] or self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserProfileSerializer(user).data,
                'message': 'Registration successful'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            login_field = serializer.validated_data['login_field']
            password = serializer.validated_data['password']
            
            # Try to find user by email or phone
            user = User.objects.filter(
                Q(email=login_field) | Q(phone=login_field)
            ).first()

            if user and user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': UserProfileSerializer(user).data,
                    'message': 'Login successful'
                })
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def forgot_password(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            login_field = serializer.validated_data['login_field']
            new_password = serializer.validated_data['new_password']

            user = User.objects.filter(
                Q(email=login_field) | Q(phone=login_field)
            ).first()

            if user:
                user.set_password(new_password)
                user.save()
                return Response({
                    'message': 'Password updated successfully'
                })
            return Response({
                'error': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
