from typing import Any
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils import translation
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from .models import Budget
from .forms import BudgetItemsFormset


class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budgets/home.html'
    context_object_name = 'budgets'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Budget.objects.filter(creator=user).order_by('-date_created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Budgets"
        return context
        

class BudgetDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Budget

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Budget Details"
        return context
    
    def test_func(self):
        budget = self.get_object()
        if self.request.user == budget.creator:
            return True
        else:
            return False
        

class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    fields = ['name', 'limit']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_creating'] = True
        context["title"] = "Create Budget"
        return context

    def form_valid(self, form) -> HttpResponse:
        form.instance.creator = self.request.user

        messages.success(
            self.request, 
            message=f"Budget '{form.instance.name}' has been created!")

        return super().form_valid(form)

    
class BudgetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Budget
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Budget"
        return context
    
    def test_func(self):
        budget = self.get_object()
        if self.request.user == budget.creator:
            return True
        else:
            return False
        
    def get_success_url(self):
        budget_name = self.object.name 
        messages.success(self.request, f'Budget "{budget_name}" has been deleted successfully.')
        return reverse_lazy('budgets-home')

class BudgetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Budget
    fields = ['name', 'limit']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_creating'] = False
        context["title"] = "Edit Budget"
        return context
    
    def test_func(self):
        budget = self.get_object()
        if self.request.user == budget.creator:
            return True
        else:
            return False
        
    def form_valid(self, form):
        messages.success(self.request, f'Budget "{form.instance.name}" has been successfully updated.')
        return super().form_valid(form)
    

class EditBudgetItemsView(LoginRequiredMixin, UserPassesTestMixin, SingleObjectMixin, FormView):
    model = Budget
    template_name = 'budgets/budget_items_edit.html'

    def test_func(self):
        budget = self.get_object()
        return self.request.user == budget.creator
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Items"
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Budget.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Budget.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return BudgetItemsFormset(**self.get_form_kwargs(), instance=self.object)
    
    def form_valid(self, form) -> HttpResponse:
        formset = self.get_form()
        if formset.is_valid():
            formset.save()
            messages.success(self.request, f'{form.instance.name} items have been successfully updated!')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        return reverse('budgets-detail', kwargs={'pk': self.object.pk})

