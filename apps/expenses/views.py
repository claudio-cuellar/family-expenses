from rest_framework import viewsets
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        This view should return a list of all the top-level categories
        for the currently authenticated user and default categories.
        Subcategories are available under the 'subcategories' field.
        """
        from django.db.models import Q
        return Category.objects.filter(
            Q(user=self.request.user) | Q(user__isnull=True, is_default=True),
            parent__isnull=True
        )


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the transactions
        for the currently authenticated user.
        """
        return Transaction.objects.filter(user=self.request.user)