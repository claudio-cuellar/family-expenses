from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_at')
    search_fields = ('email', 'name')

# Register your models here.