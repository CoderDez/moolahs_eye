from django.urls import path
from .views import (
    BudgetListView,
    BudgetCreateView,
    BudgetDeleteView,
    BudgetUpdateView,
    BudgetDetailView,
    EditBudgetItemsView
)


urlpatterns = [
    path('', BudgetListView.as_view(), name='budgets-home'),
    path('budget/<int:pk>/', BudgetDetailView.as_view(), name='budgets-detail'),
    path('budget/new/', BudgetCreateView.as_view(), name='budgets-create'),
    path('budget/<int:pk>/delete/', BudgetDeleteView.as_view(), name='budgets-delete'),
    path('budget/<int:pk>/update/', BudgetUpdateView.as_view(), name='budgets-update'),
    path('budget/<int:pk>/items/edit', EditBudgetItemsView.as_view(), name='edit-items'),
]