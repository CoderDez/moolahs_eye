from django.urls import path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .views import CalculatorView, CurrencyConverterView

urlpatterns = [
    path("calculator/", CalculatorView.as_view(), name='calculator'),
    path("currency-converter/", CurrencyConverterView.as_view(), name='currency-converter')
]