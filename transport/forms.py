from django import forms
from .models import Trips, Expense,TransportExpenses

class TripForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['starting_km', 'ending_km', 'money_collected', 'is_online_payment', 'transaction_id', 'expenses', 'diesel']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name']

class TransportExpensesForm(forms.ModelForm):
    class Meta:
        model = TransportExpenses
        fields = ['name', 'amount']
