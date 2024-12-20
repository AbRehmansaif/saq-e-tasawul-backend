from django.db import models
from django.utils.translation import gettext_lazy as _
from order_details.models import OrderDetails
from shipping.enums import ShippingMethod


class ShippingDetails(models.Model):
    class Meta:
        verbose_name = _('Shipping Detail')
        verbose_name_plural = _('Shipping Details')
    
    order = models.OneToOneField(
        OrderDetails, on_delete=models.CASCADE, 
        related_name='shipping'
    )
    address_line_1 = models.CharField(
        max_length=255, null=True,
        blank=True
    )
    address_line_2 = models.CharField(
        max_length=255, blank=True,
        null=True
    )
    country = models.CharField(
        max_length=100, null=True,
        blank=True
    )
    city = models.CharField(
        max_length=100, null=True,
        blank=True
    )
    postal_code = models.CharField(
        max_length=20, null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=15, null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True,
        blank=True
    )
    shipping_method = models.CharField(
        max_length=50, 
        choices=ShippingMethod.choices(),
        default=ShippingMethod.STANDARD.value
    )
    tracking_url = models.URLField(
        blank=True
    )
    estimated_delivery = models.DateField(
        null=True
    )
    shipping_instructions = models.TextField(
        blank=True
    )