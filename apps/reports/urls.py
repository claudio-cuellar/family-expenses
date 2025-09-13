from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('income-vs-expense-summary/', views.IncomeVsExpenseSummaryView.as_view(), name='income-vs-expense-summary'),
    path('expenses-by-category/', views.ExpensesByCategoryView.as_view(), name='expenses-by-category'),
]