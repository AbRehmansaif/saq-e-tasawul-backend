from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name='products'
    )
    producat_name = models.CharField(
        max_length=255, null=True,
        blank=True
    )
    description = models.TextField(
        null=True, blank=True
    )
    quantity = models.PositiveBigIntegerField(
        default=0 ,null=True, 
        blank=True
    )
    status = models.CharField(
        max_length=20, null=True,
        blank=True
    )
    coupon = models.CharField(
        max_length=20, null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, blank=True
    )
    trend = models.BooleanField(
        default=False
    )
    rate = models.DecimalField(
        max_digits=5, decimal_places=2, 
        null=True, blank=True
    )
    max_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True
    )
    selling_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True
    )
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    comments = models.TextField(
        blank=True, null=True
    )
    sku = models.CharField(
        max_length=50, unique=True
    )
    brand = models.CharField(
        max_length=100
    )
    weight = models.DecimalField(
        max_digits=10, decimal_places=2, 
        null=True
    )
    dimensions = models.CharField(
        max_length=50, blank=True
    )
    meta_title = models.CharField(
        max_length=200, blank=True
    )
    meta_description = models.TextField(
        blank=True
    )
    slug = models.SlugField(
        unique=True
    )
    tags = models.JSONField(
        default=list, blank=True
    )  # For better search and categorization
    features = models.JSONField(
        default=dict
    )  # Store product features for AI recognition
    view_count = models.PositiveIntegerField(
        default=0
    )  # For popularity tracking
    purchase_count = models.PositiveIntegerField(
        default=0
    )  # For demand analysis