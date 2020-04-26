from django import forms
from .models import Order
from checkout.choices import months, years


class MakePaymentForm(forms.Form):
    # MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    # YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

    credit_card_number = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Credit Card Number'
        })
    )

    cvv = forms.IntegerField(
        required=False,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Security Code (CVV)'
        })
    )

    expiry_month = forms.ChoiceField(
        required=False,
        label='',
        choices=months,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    expiry_year = forms.ChoiceField(
        required=False,
        label='',
        choices=years,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    stripe_id = forms.CharField(
        widget=forms.HiddenInput
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {
            'full_name',
            'email'
        }

    full_name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Full Name'
        })
    )

    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        })
    )
