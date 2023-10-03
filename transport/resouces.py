from import_export import resources
from .models import TransportExpenses, Trips, Expense


class TransportExpensesResource(resources.ModelResource):
    class Meta:
        model = TransportExpenses


class TripsResource(resources.ModelResource):
    class Meta:
        model = Trips


class ExpenseResource(resources.ModelResource):
    class Meta:
        model = Expense
