from django import forms

from .models import Rental, House


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['house', 'rent_amount', 'rent_paid', 'tenant_name', 'mobile_number']


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address']
