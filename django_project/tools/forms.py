from django.forms import Form
from django import forms
from .models import Currency

class CalculatorForm(Form):
    """
    Form for a simple calculator.

    Fields:
    - expression (CharField): Field to input and display the expression.
    """

    expression = forms.CharField(
        label="",
        max_length=32, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control disabled-input', 
                'readonly': True
            }
        )
    )
    
    def __init__(self, *args, **kwargs):
        expression = kwargs.pop('expression', None) 
        super().__init__(*args, **kwargs)

        if expression is not None:
            self.initial['expression'] = expression


class CurrencyConverterForm(Form):
    """
    Form for currency conversion.

    Fields:
    - amount (DecimalField): Field for entering the amount to convert.
    - from_currency (ChoiceField): Field for selecting the currency to convert from.
    - to_currency (ChoiceField): Field for selecting the currency to convert to.
    - figure (DecimalField): Field to display the converted amount (disabled).
    """
    currencies = [(currency.symbol, currency.desc) for currency in Currency.objects.all()]
    amount = forms.DecimalField(max_digits=12, label="Amount", decimal_places=2)
    from_currency = forms.ChoiceField(choices=currencies, label="From")
    to_currency = forms.ChoiceField(choices=currencies, label="To")

    figure = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        label="Figure",
        disabled=True, 
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control disabled-input bg-light', 
            }
            ))
    
    def __init__(self, *args, **kwargs):
        initial_figure = kwargs.pop('initial_figure', None) 
        super().__init__(*args, **kwargs)

        if initial_figure is not None:
            self.initial['figure'] = initial_figure
    