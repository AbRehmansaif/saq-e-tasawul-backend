from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import Category


class SubCategory(models.Model):
    class Meta:
        verbose_name = _('Sub Category')
        verbose_name_plural = _('Sub Categories')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_categories'
    )
    name = models.CharField(
        max_length=100, blank=True,
        null=True
    )
    description = models.TextField(
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True
    )
    image = models.ImageField(
        upload_to='sub_category_image', blank=True, 
        null=True
    )
    is_active = models.BooleanField(
        default=True
    )
    meta_title = models.CharField(
        max_length=200, blank=True, 
        null=True
    )
    meta_description = models.TextField(
        blank=True, null=True
    )
    slug = models.SlugField(
        unique=True
    )
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"