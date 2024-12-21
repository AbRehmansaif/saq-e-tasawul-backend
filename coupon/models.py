from django.db import models
from django.utils.translation import gettext_lazy as _
from product.models import Product


class Coupon(models.Model):
    class Meta():
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')
    
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, 
        related_name='coupons'
    )
    coupon = models.CharField(
        max_length=50, unique=True
    )
    quantity = models.PositiveIntegerField(
        default=0
    )
    discount_type = models.CharField(
        max_length=20
    )  # percentage or fixed
    discount_value = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    minimum_purchase = models.DecimalField(
        max_digits=10, decimal_places=2, 
        null=True
    )
    is_active = models.BooleanField(
        default=True
    )
    usage_limit = models.PositiveIntegerField(
        default=1
    )
    times_used = models.PositiveIntegerField(
        default=0
    )