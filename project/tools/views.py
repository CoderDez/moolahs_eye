from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CalculatorForm, CurrencyConverterForm
from .currency_converter import perform_exchange
from decimal import Decimal

import requests, os
from .models import Currency


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
    success_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        context["title"] = "Currency Converter"
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST)
        context = self.get_context_data()

        if form.is_valid():
            amount = Decimal(form.cleaned_data.get('amount'))
            from_currency_symbol = form.cleaned_data.get('from_currency')
            to_currency_symbol = form.cleaned_data.get('to_currency')

            # Retrieve Currency instances based on selected symbols
            from_currency = Currency.objects.get(symbol=from_currency_symbol)
            to_currency = Currency.objects.get(symbol=to_currency_symbol)

            if from_currency == to_currency:
                initial_figure = amount
            else:
                initial_figure = perform_exchange(from_currency.symbol, to_currency.symbol, amount)

            form = self.form_class(request.POST, initial_figure=initial_figure)
         
        context['form'] = form

        return render(request, self.template_name, context)