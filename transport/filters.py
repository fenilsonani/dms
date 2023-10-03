import django_filters

from .models import TransportExpenses, Expense, Trips


class TransportExpensesFilter(django_filters.FilterSet):
    # Your filtering fields for TransportExpenses
    class Meta:
        model = TransportExpenses
        fields = ['name', 'amount', 'date']  # replace with your fields


class ExpenseFilter(django_filters.FilterSet):
    # Your filtering fields for Expense
    class Meta:
        model = Expense
        fields = ['name']  # replace with your fields


class TripsFilter(django_filters.FilterSet):
    # Your filtering fields for Trips
    class Meta:
        model = Trips
        fields = ['starting_km', 'ending_km', 'date','transaction_id']  # replace with your fields
