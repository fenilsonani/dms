import django_filters

from .models import Customer, DailyProduction, Animal, Labor, Expense, Grass, Payment, DailyDelivery


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['name', 'location', 'mobile_number']


class DailyProductionFilter(django_filters.FilterSet):
    class Meta:
        model = DailyProduction
        fields = ['date', 'milk', 'amount', 'payment', 'customer']


class AnimalFilter(django_filters.FilterSet):
    class Meta:
        model = Animal
        fields = ['name', 'location', 'mobile_number']


class LaborFilter(django_filters.FilterSet):
    class Meta:
        model = Labor
        fields = ['name', 'location', 'mobile_number']


class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date']


class GrassFilter(django_filters.FilterSet):
    class Meta:
        model = Grass
        fields = ['location', 'owner_name', 'owner_mobile', 'total_amount_grass', 'rate', 'final_price', 'due_amount',
                  'amount_to_be_paid']


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = ['customer', 'amount', 'date']


class DailyDeliveryFilter(django_filters.FilterSet):
    class Meta:
        model = DailyDelivery
        fields = ['date', 'milk', 'amount', 'payment', 'customer']
