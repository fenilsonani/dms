from django.shortcuts import render

from .forms import TripForm, ExpenseForm, TransportExpensesForm
from .models import Trips, TransportExpenses, Expense
from .filters import TripsFilter,TransportExpensesFilter,ExpenseFilter

def create_trip(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            trip_form = TripForm(request.POST)
            if trip_form.is_valid():
                trip = trip_form.save()
                # Do something with the saved trip object
                message = 'Trip added successfully'
                context = {'trip_form': trip_form, 'message': message}
                return render(request, 'transport/add_trip.html', context)
        else:
            trip_form = TripForm()
            error = trip_form.errors
            context = {'trip_form': trip_form, 'error': error, 'message': 'Trip not added'}
            return render(request, 'transport/add_trip.html', context)
        context = {'trip_form': trip_form}
        return render(request, 'transport/add_trip.html', context)


def create_expense(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense = expense_form.save()
                # Do something with the saved expense object
                message = 'Expense added successfully'
                context = {'expense_form': expense_form, 'message': message}
                return render(request, 'transport/create_expense.html', context)
            else:
                message = 'Expense not added'
                context = {'expense_form': expense_form, 'message': message}
                return render(request, 'transport/create_expense.html', context)
        else:
            expense_form = ExpenseForm()
        context = {'expense_form': expense_form}
        return render(request, 'transport/create_expense.html', context)


def add_expense(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            expense_form = TransportExpensesForm(request.POST)
            if expense_form.is_valid():
                expense = expense_form.save()
                # Do something with the saved expense object
                #         add message to context
                message = 'Expense added successfully'
                context = {'expense_form': expense_form,
                           'message': message
                           }
                return render(request, 'transport/add_expense.html', context)
        else:
            expense_form = TransportExpensesForm()
            error = expense_form.errors
            context = {'expense_form': expense_form, 'error': error, 'message': 'Expense not added'}

        context = {'expense_form': expense_form}
        return render(request, 'transport/add_expense.html', context)


def display_trips(request):
    if request.user.is_authenticated:
        trips = TripsFilter(request.GET, queryset=Trips.objects.all())
        context = {'trips': trips}
        return render(request, 'transport/display/trips.html', context)
    else:
        return render(request, 'users/not_loggedin.html')


def display_expenses_type(request):
    if request.user.is_authenticated:
        expenses = ExpenseFilter(request.GET, queryset=Expense.objects.all())
        context = {'expenses': expenses}
        return render(request, 'transport/display/expenses_type.html', context)
    else:
        return render(request, 'users/not_loggedin.html')


def display_expenses(request):
    if request.user.is_authenticated:
        expenses = TransportExpensesFilter(request.GET, queryset=TransportExpenses.objects.all())
        context = {'expenses': expenses}
        return render(request, 'transport/display/expenses.html', context)
    else:
        return render(request, 'users/not_loggedin.html')


def edit_trip(request, trip_id):
    if request.user.is_authenticated:
        trip = Trips.objects.get(id=trip_id)
        if request.method == 'POST':
            trip_form = TripForm(request.POST, instance=trip)
            if trip_form.is_valid():
                trip_form.save()
                # Do something with the saved trip object
        else:
            trip_form = TripForm(instance=trip)

        context = {'trip_form': trip_form}
        return render(request, 'transport/edit/trips.html', context)
    else:
        return render(request, 'users/not_loggedin.html')


def edit_expense(request, expense_id):
    if request.user.is_authenticated:
        expense = TransportExpenses.objects.get(id=expense_id)
        if request.method == 'POST':
            expense_form = TransportExpensesForm(request.POST, instance=expense)
            if expense_form.is_valid():
                expense_form.save()
                # Do something with the saved expense object
        else:
            expense_form = TransportExpensesForm(instance=expense)

        context = {'expense_form': expense_form}
        return render(request, 'transport/edit/expenses.html', context)
    else:
        return render(request, 'users/not_loggedin.html')


def edit_expense_type(request, expense_id):
    if request.user.is_authenticated:
        expense = Expense.objects.get(id=expense_id)
        if request.method == 'POST':
            expense_form = ExpenseForm(request.POST, instance=expense)
            if expense_form.is_valid():
                expense_form.save()
                # Do something with the saved expense object
        else:
            expense_form = ExpenseForm(instance=expense)

        context = {'expense_form': expense_form}
        return render(request, 'transport/edit/expenses_type.html', context)
    else:
        return render(request, 'users/not_loggedin.html')


def delete_trip(request, trip_id):
    if request.user.is_authenticated:
        trip = Trips.objects.get(id=trip_id)
        trip.delete()
        return render(request, 'transport/display/trips.html')
    else:
        return render(request, 'users/not_loggedin.html')


def delete_expense(request, expense_id):
    if request.user.is_authenticated:
        expense = TransportExpenses.objects.get(id=expense_id)
        expense.delete()
        return render(request, 'transport/display/expenses.html')
    else:
        return render(request, 'users/not_loggedin.html')


def delete_expense_type(request, expense_id):
    if request.user.is_authenticated:
        expense = Expense.objects.get(id=expense_id)
        expense.delete()
        return render(request, 'transport/display/expenses_type.html')
    else:
        return render(request, 'users/not_loggedin.html')
