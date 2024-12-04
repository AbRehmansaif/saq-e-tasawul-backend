from django.db import models
from django.utils.translation import gettext_lazy as _
from order_details.models import Order_detail


class Payment(models.Model):
    class Meta():
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        
    id = models.AutoField(
        primary_key=True, verbose_name = _('ID')
    )
    
    order_id = models.ForeignKey(
        Order_detail.order_id, on_delete=models.CASCADE, 
        verbose_name = _('Order ID')
    )
    
    amount = models.ForeignKey(
        Order_details.total_payment, on_delete=models.CASCADE,
        verbose_name = _('Amount')
    )
    
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        verbose_name = _('User ID')
    )
    
    status = models.BooleanField(
        default=False, verbose_name = _('Status')
    )