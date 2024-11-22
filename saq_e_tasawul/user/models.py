from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    email = models.EmailField(
        unique=True,
        verbose_name=_("E-mail")
    )
    
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name=_("First Name")
    )
    
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name=_("Last Name")
    )
       
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active Status")
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups", 
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
    )
    
    def __str__(self):
        return self.get_full_name() or self.username

