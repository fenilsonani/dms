from django import forms

from .models import House, RentPayment, RentalPerson


class RentPaymentForm(forms.ModelForm):
    class Meta:
        model = RentPayment
        fields = "__all__"

    def save(self):
        pass


class RentalPersonForm(forms.ModelForm):
    class Meta:
        model = RentalPerson
        fields = "__all__"


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address']
