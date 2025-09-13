from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import services

class IncomeVsExpenseSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = services.get_income_vs_expense_summary(request.user)
        return Response(data)


class ExpensesByCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = services.get_expenses_by_category(request.user)
        return Response(data)