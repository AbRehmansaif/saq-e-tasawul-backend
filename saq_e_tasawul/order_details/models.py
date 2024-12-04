from django.db import models
from django.utils.translation import gettext_lazy as _


class Order_detail(models.Model):
    class Meta():
        verbose_name = _('Order detail')
        verbose_name_plural = _('Order details')
        
    user_id = model.ForeignKey(
        'auth.User', on_delete=models.CASCADE, 
        verbose_name=_('User'),
    )
    
    payment_id = models.ForeignKey(
        'payment.Payment', on_delete=models.CASCADE,
        verbose_name=_('Payment')
    )
    
    order_id = models.ForeignKey(
        'order.Order', on_delete=models.CASCADE,
        verbose_name=_('Order')
    )
    
    total_orders = models.IntegerField(
        verbose_name= _('Total orders')
    )
    
    total_payment = models.ForeignKey(
        'payment.Payment', on_delete=models.CASCADE,
        verbose_name=_('Total payment')
    )
    
    status = models.Boolean(
        
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )
    
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at')
    )