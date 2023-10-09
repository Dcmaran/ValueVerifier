from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ConversionForm(forms.Form):
    amount = forms.DecimalField(
        label='Value',
        widget=forms.NumberInput(attrs={'id': 'amount'}),
        validators=[
            MinValueValidator(0, message='Amount cannot be negative.'),
            MaxValueValidator(10000, message='Amount cannot exceed 10000.'),
        ]
    )
    
    CURRENCY_CHOICES = [
        ('BRL', 'Brazilian Real (BRL)'),
        ('USD', 'US Dollar (USD)'),
        ('EUR', 'Euro (EUR)'),
        ('GBP', 'British Pound (GBP)'),
        ('JPY', 'Japanese Yen (JPY)'),
        ('CAD', 'Canadian Dollar (CAD)'),
        ('AUD', 'Australian Dollar (AUD)'),
    ]
    
    from_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label='From:', widget=forms.Select(attrs={'class': 'from_currency'}))
    to_currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label='To:', widget=forms.Select(attrs={'class': 'to_value'}))
