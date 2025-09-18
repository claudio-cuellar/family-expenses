from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Fields to display in the user list
    list_display = ('email', 'username', 'first_name', 'last_name', 'family_role', 'is_staff', 'is_active')
    list_filter = ('family_role', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    
    # Fields to show when editing a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture')}),
        ('Family', {'fields': ('family_role',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to show when adding a new user - NOW INCLUDES profile_picture
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'profile_picture'),
        }),
        ('Family', {
            'classes': ('wide',),
            'fields': ('family_role',),
        }),
    )
    
    # Make email the primary identifier
    readonly_fields = ('date_joined', 'last_login')