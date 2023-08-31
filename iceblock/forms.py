from django import forms
from .models import Customer, Delivery

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone_number']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['customer', 'date', 'daily_ice_block_given', 'one_ice_block_price', 'total_ice_block_price', 'additional_transportation_charge','total_charge']
