from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CalculatorForm, CurrencyConverterForm


class CalculatorView(FormView):
    template_name = "tools/calculator.html"
    form_class = CalculatorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context["title"] = "Calculator"
        return context

class CurrencyConverterView(FormView):
    template_name = "tools/currency_converter.html"
    form_class = CurrencyConverterForm

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return super().post(self, request, *args, **kwargs)
