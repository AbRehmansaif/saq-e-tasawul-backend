from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.v2.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('auth/complete-profile/', UserViewSet.as_view({'put': 'complete_profile'}), name='complete-profile'),
]