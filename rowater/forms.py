from django.forms import ModelForm

from .models import Customer, Delivery


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'
