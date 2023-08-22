from django import forms

class ConversionForm(forms.Form):
    input = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.CharField(max_length=3)
    converted_currency = forms.CharField(max_length=3)