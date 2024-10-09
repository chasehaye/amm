from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('id', 'email', 'name', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'is_admin')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_admin')}
        ),
    )
    search_fields = ('email', 'name')
    ordering = ('-is_admin', 'email')

# Register the new UserAdmin
admin.site.register(User, UserAdmin)