from django.db import models
from django.utils.translation import gettext_lazy as _


class Coupon(models.Model):
    class Meta():
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')
    
    product_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE, 
        verbose_name=_('Product')
    )
    
    coupon_code = models.CharField(
        max_length=255, verbose_name=_('Coupon Code')
    )
    
    quantity = models.IntegerField(
        verbose_name=_('Quantity')
    )