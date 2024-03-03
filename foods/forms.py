from django import forms
from .models import Order


class OrderForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your address')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your phone')

    class Meta:
        model = Order
        fields = ['phone', 'address']