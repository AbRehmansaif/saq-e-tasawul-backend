from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from product.models import Product
from order_details.enums import OrderStatus


class Order(models.Model):
    class Meta():
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, 
        verbose_name=_('User')
    )
    order_number = models.CharField(
        max_length=50, unique=True,
        verbose_name=_('Order number')
    )
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE,
        verbose_name=_('Product')
    )
    quantity = models.IntegerField(
        default=1
    )
    ordered_at = models.DateTimeField(
        auto_now_add=True
    )
    total_payment = models.DecimalField(
        max_digits=10, decimal_places=2, 
        default=0
    )
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices(), 
        default=OrderStatus.PENDING.value[0],
        verbose_name=_('Status')
    )
    tracking_number = models.CharField(
        max_length=100, blank=True
    )
    estimated_delivery = models.DateField(
        null=True, blank=True,
        verbose_name=_('Estimated Delivery')
    )
    
class OrderDetails(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE,
        related_name='details'
    )
    payment_id = models.CharField(
        max_length=100, null=True,
        blank=True
    )
    transaction_id = models.CharField(
        max_length=100, null=True,
        blank=True
    )
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices(), 
        default=OrderStatus.PENDING.value
    )
    notes = models.TextField(
        blank=True
    )
    gift_wrap = models.BooleanField(
        default=False
    )
    gift_message = models.TextField(
        blank=True
    )