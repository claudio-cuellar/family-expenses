from rest_framework import serializers
from .models import Category, Transaction

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = ['id', 'name']

    def create(self, validated_data):
        """
        Associate the category with the current user upon creation.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.
    """
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Transaction
        fields = [
            'id', 'transaction_type', 'amount', 'category', 'date', 'notes'
        ]

    def create(self, validated_data):
        """
        Associate the transaction with the current user upon creation.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def __init__(self, *args, **kwargs):
        """
        Filter the category queryset to only show categories owned by the
        current user.
        """
        super().__init__(*args, **kwargs)
        if self.context:
            request = self.context.get('request')
            if request and hasattr(request, 'user'):
                self.fields['category'].queryset = Category.objects.filter(
                    user=request.user
                )