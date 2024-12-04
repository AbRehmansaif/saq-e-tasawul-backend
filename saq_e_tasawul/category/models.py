from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        
    id = models.AutoField(
        primary_key=True
    )
    
    name = models.CharField(
        max_length=255, verbose_name=_('Category Name')
    )
    
    description = models.TextField(
        verbose_name=_('Category Description')
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created At')
    )
    
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated At')
    )