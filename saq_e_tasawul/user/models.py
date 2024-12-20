from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    phone = models.CharField(
        max_length=15, blank=True
    )
    email_verify = models.BooleanField(
        default=False
    )
    first_name = models.CharField(
        max_length=150, blank=True
    )
    last_name = models.CharField(
        max_length=150, blank=True
    )
    status = models.CharField(
        max_length=20, default='active'
    )
    profile_image = models.ImageField(
        upload_to='profile_images/', null=True, 
        blank=True
    )
    address = models.TextField(
        blank=True
    )
    newsletter_subscription = models.BooleanField(
        default=False
    )
    preferences = models.JSONField(
        default=dict, blank=True
    )  # Store user preferences for recommendations
    search_history = models.JSONField(
        default=list, blank=True
    )  # Store search history for better recommendations