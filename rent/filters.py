import django_filters

from .models import RentalPerson, House, RentPayment


class RentalPersonFilter(django_filters.FilterSet):
    # Your filtering fields for RentalPerson
    class Meta:
        model = RentalPerson
        fields = ['name', 'house', 'phone_number']  # replace with your fields


class HouseFilter(django_filters.FilterSet):
    # Your filtering fields for House
    class Meta:
        model = House
        fields = ['name', 'address']  # replace with your fields


class RentPaymentFilter(django_filters.FilterSet):
    # Your filtering fields for RentPayment
    class Meta:
        model = RentPayment
        fields = ['rental_person', 'date', 'payment_method', 'payment_id']
