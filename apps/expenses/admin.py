from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category, Transaction

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    """
    Admin configuration for the Category model.
    """
    list_display = ('name', 'user')
    search_fields = ('translations__name',)
    list_filter = ('user',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Transaction model.
    """
    list_display = ('user', 'transaction_type', 'amount', 'category', 'date')
    search_fields = ('notes',)
    list_filter = ('user', 'transaction_type', 'category', 'date')
    autocomplete_fields = ('category',)