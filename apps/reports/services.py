from django.db.models import Sum, Count, Q, F, Subquery, OuterRef
from django.db.models.functions import TruncMonth
from apps.expenses.models import Transaction, Category

def get_income_vs_expense_summary(user):
    """
    Returns a summary of income vs. expenses per month for a given user.
    """
    return Transaction.objects.filter(user=user).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total_income=Sum('amount', filter=Q(transaction_type=Transaction.TransactionType.INCOME)),
        total_expense=Sum('amount', filter=Q(transaction_type=Transaction.TransactionType.OUTCOME))
    ).order_by('month')

def get_expenses_by_category(user):
    """
    Returns a summary of expenses by category for a given user.
    """
    CategoryTranslation = Category.translations.rel.related_model
    category_name_subquery = Subquery(
        CategoryTranslation.objects.filter(
            master_id=OuterRef('category_id')
        ).order_by('language_code').values('name')[:1]
    )
    return Transaction.objects.filter(
        user=user,
        transaction_type=Transaction.TransactionType.OUTCOME,
        category__isnull=False
    ).annotate(
        category_name=category_name_subquery
    ).values('category_name').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')