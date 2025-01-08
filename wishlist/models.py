from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from product.models import Product


class Wishlist(models.Model):
    class Meta:
        verbose_name = _('Wishlist')
        verbose_name_plural = _('Wishlists')
        
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, 
        related_name='favorites'
    )
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, 
        related_name='favorited_by'
    )
    added_at = models.DateTimeField(
        auto_now_add=True
    )
    notification_enabled = models.BooleanField(
        default=False
    )  # Notify when price drops
        
    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"