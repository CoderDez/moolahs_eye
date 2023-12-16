from django.forms import Form
from django import forms

class CalculatorForm(Form):
    text_input = forms.CharField(
        label="",
        max_length=32, 
        disabled=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control disabled-input', 
            }
            )
    )


class CurrencyConverterForm(Form):
    currencies = [
        ('EUR', 'Euro €'),
        ('USD', 'US Dollar $'),
        ('GBP', 'British Pound £'),
        ('AUD', 'Australian Dollar $'),
        ('CAD', 'Candadian Dollar $'),
        ('CHF', 'Swiss Franc ₣'),
        ('CNY', 'Chinese Yuan ¥' ),
        ('JPY', 'Japanese Yen ¥')
        # Add more currencies as needed
    ]

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
    