from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import Category, Transaction

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(TranslatableModelSerializer):
    """
    Serializer for the Category model.
    """
    translations = TranslatedFieldsField(shared_model=Category)
    subcategories = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'translations', 'parent', 'subcategories', 'icon']

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