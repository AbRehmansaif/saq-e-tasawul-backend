from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
    email = models.EmailField(
        unique=True
    )
    phone = models.CharField(
        max_length=15, unique=True
    )
    address = models.TextField(
        blank=True
    )
    city = models.CharField(
        max_length=100, blank=True
    )
    country = models.CharField(
        max_length=100, blank=True
    )
    postal_code = models.CharField(
        max_length=20, blank=True
    )
    profile_completed = models.BooleanField(
        default=False
    )
    profile_image = models.ImageField(
        upload_to='profile_images/', null=True, blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

