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
                'readonly': 'readonly'}
            )
    )


class CurrencyConverterForm(Form):
    pass