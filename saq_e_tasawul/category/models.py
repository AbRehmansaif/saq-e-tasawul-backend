from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
    name = models.CharField(
        max_length=255, verbose_name=_('Category Name')
    )
    description = models.TextField(
        verbose_name=_('Category Description')
    )
    image = models.ImageField(
        upload_to='category_image', null=True
    )
    is_active = models.BooleanField(
        default=True, verbose_name=_('Is Active')
    )
    meta_title = models.CharField(
        max_length=200, blank=True
    )  # For SEO
    meta_description = models.TextField(
        blank=True
    )  # For SEO
    slug = models.SlugField(
        unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created At')
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated At')
    )