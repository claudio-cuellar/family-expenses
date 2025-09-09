from django.db import models
from django.conf import settings

class Category(models.Model):
    """
    Represents a category for a transaction, e.g., "Groceries", "Salary".
    """
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    def __str__(self):
        return self.name

class Transaction(models.Model):
    """
    Represents a single financial transaction, which can be either an
    income or an outcome.
    """
    class TransactionType(models.TextChoices):
        INCOME = 'IN', 'Income'
        OUTCOME = 'OUT', 'Outcome'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    transaction_type = models.CharField(
        max_length=3,
        choices=TransactionType.choices,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transactions'
    )
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} of {self.amount} on {self.date}"