from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.auth.v2.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserViewSet.as_view({'post': 'register'}), name='register'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('forget-password/', UserViewSet.as_view({'post': 'forgot_password'}), name='forgot-password')
]