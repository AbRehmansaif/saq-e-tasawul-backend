from django.db import models
from django.utils.translation import gettext_lazy as _
from order_details.models import OrderDetails
from payment.enums import PaymentStatus


class Payment(models.Model):
    class Meta():
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
    
    order = models.OneToOneField(
        OrderDetails, on_delete=models.CASCADE, 
        related_name='payment'
    )
    amount = models.ForeignKey(
        OrderDetails.total_payment, on_delete=models.CASCADE,
        verbose_name = _('Amount')
    )
    status = models.BooleanField(
        max_length=20,
        choices=PaymentStatus.choices(),
        default=PaymentStatus.PENDING.value
    )
    payment_method = models.CharField(
        max_length=50, null=True, 
        blank=True
    )
    transaction_id = models.CharField(
        max_length=100, unique=True
    )
    payment_date = models.DateTimeField(
        auto_now_add=True, blank=True
    )