import django_filters

from .models import Customer, Delivery


class CustomerFilter(django_filters.FilterSet):
    # Your filtering fields for Customer
    class Meta:
        model = Customer
        fields = ['name', 'address','phone_number']  # replace with your fields


class DeliveryFilter(django_filters.FilterSet):
    # Your filtering fields for Delivery
    class Meta:
        model = Delivery
        fields = ['customer', 'date','daily_ice_block_given']  # replace with your fields
