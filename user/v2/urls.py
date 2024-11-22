from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [

    path('', include(router.urls)),


    path('auth/register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('auth/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('auth/logout/', UserViewSet.as_view({'post': 'logout'}), name='user-logout'),
]
