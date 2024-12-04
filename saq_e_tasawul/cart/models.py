from django.db import models
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
        
    id = models.AutoField(
        primary_key=True
    )
    
    user_id = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, 
        related_name='cart_user_id'
    )
    
    total_products = models.IntegerField(
        default=0, verbose_name=_('Total products')
    )
    
    products_id = models.ManyToManyField(
        'products.Product', related_name='cart_products'
    )