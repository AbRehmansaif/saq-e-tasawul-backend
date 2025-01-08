from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from product.models import Product


class CartItem(models.Model):
    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')
    
    cart = models.ForeignKey(
        'Cart', 
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cart.id} - {self.product.name} ({self.quantity})"
    
    
class Cart(models.Model):
    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_('User'),
        related_name='carts'
    )
    total_products = models.PositiveBigIntegerField(
        default=0, 
        null=True,
        blank=True
    )
    products = models.ManyToManyField(
        Product, 
        through=CartItem,  # Changed from 'Order' to CartItem
        related_name='carts'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        blank=True,
        null=True
    )
    session_id = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )  # For anonymous users
    total_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0
    )
    
    def __str__(self):
        return f"Cart {self.id} - {self.user.username}"