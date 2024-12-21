from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from product.models import Product


class Cart(models.Model):
    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('User')
    )
    total_products = models.PositiveBigIntegerField(
        default=0, null=True,
        blank=True
    )
    products = models.ManyToManyField(
        Product, through='Order'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, blank=True,
        null=True
    )
    session_id = models.CharField(
        max_length=100
    )  # For anonymous users
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, 
        default=0
    )