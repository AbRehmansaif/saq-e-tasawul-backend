from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# from .models import User
from django.contrib.auth import get_user_model


User = get_user_model() 

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    list_display = (
        'username', 'email', 
        'first_name', 'last_name', 
        'is_active', 'date_joined'
    ) 
    
    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': [
                'is_active'
            ]
        }),
        (_('Important dates'), {
            'fields': ['created_at', 'updated_at']
        }),
    )
    

# admin.site.register(User, CustomUserAdmin)