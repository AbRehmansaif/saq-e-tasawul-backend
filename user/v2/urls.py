from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.v2.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', UserViewSet.as_view({'post': 'register'}), name='register'),
    path('auth/login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('auth/forgot-password/', UserViewSet.as_view({'post': 'forgot_password'}), name='forgot-password'),
    path('auth/complete-profile/', UserViewSet.as_view({'put': 'complete_profile'}), name='complete-profile'),
]