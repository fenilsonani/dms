from django.shortcuts import render

from .forms import AnimalForm, LaborForm, ExpenseForm, GrassForm, CustomerFormCreate, DailyDeliveryForm, \
    DailyProductionForm, PaymentForm, CustomerFormUpdate

CustomerFormUpdate, PaymentForm
from .models import Animal, Labor, Expense, Grass, Customer, DailyDelivery, DailyProduction, Payment


# Create your views here.

def create_animal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AnimalForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/animal.html', {'form': form, 'message': 'Animal Added Successfully'})
            else:
                return render(request, 'milkfarm/animal.html', {'form': form, 'message': 'Animal Not Added'})
        else:
            form = AnimalForm()
        return render(request, 'milkfarm/animal.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_labor(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = LaborForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/labor.html', {'form': form, 'message': 'Labor Added Successfully'})
            else:
                return render(request, 'milkfarm/labor.html', {'form': form, 'message': 'Labor Not Added'})
        else:
            form = LaborForm()
        return render(request, 'milkfarm/labor.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_expense(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/expense.html', {'form': form, 'message': 'Expense Added Successfully'})
            else:
                return render(request, 'milkfarm/expense.html', {'form': form, 'message': 'Expense Not Added'})
        else:
            form = ExpenseForm()
        return render(request, 'milkfarm/expense.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_grass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GrassForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/grass.html', {'form': form, 'message': 'Grass Added Successfully'})
            else:
                return render(request, 'milkfarm/grass.html', {'form': form, 'message': 'Grass Not Added'})
        else:
            form = GrassForm()
        return render(request, 'milkfarm/grass.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def view_animal(request):
    if request.user.is_authenticated:
        animals = Animal.objects.all()
        return render(request, 'milkfarm/display/animal.html', {'animals': animals})
    else:
        return render(request, 'users/not_loggedin.html')


def view_labor(request):
    if request.user.is_authenticated:
        labors = Labor.objects.all()
        return render(request, 'milkfarm/display/labor.html', {'labors': labors})
    else:
        return render(request, 'users/not_loggedin.html')


def view_expense(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.all()
        return render(request, 'milkfarm/display/expense.html', {'expenses': expenses})
    else:
        return render(request, 'users/not_loggedin.html')


def view_grass(request):
    if request.user.is_authenticated:
        grasses = Grass.objects.all()
        return render(request, 'milkfarm/display/grass.html', {'grasses': grasses})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_animal(request, id):
    if request.user.is_authenticated:
        animal = Animal.objects.get(id=id)
        animal.delete()
        return render(request, 'milkfarm/display/animal.html', {'message': 'Animal Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_labor(request, id):
    if request.user.is_authenticated:
        labor = Labor.objects.get(id=id)
        labor.delete()
        return render(request, 'milkfarm/display/labor.html', {'message': 'Labor Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_expense(request, id):
    if request.user.is_authenticated:
        expense = Expense.objects.get(id=id)
        expense.delete()
        return render(request, 'milkfarm/display/expense.html', {'message': 'Expense Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_grass(request, id):
    if request.user.is_authenticated:
        grass = Grass.objects.get(id=id)
        grass.delete()
        return render(request, 'milkfarm/display/grass.html', {'message': 'Grass Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def update_animal(request, id):
    if request.user.is_authenticated:
        animal = Animal.objects.get(id=id)
        if request.method == 'POST':
            form = AnimalForm(request.POST, instance=animal)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/animal.html',
                              {'form': form, 'message': 'Animal Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/animal.html', {'form': form, 'message': 'Animal Not Updated'})
        else:
            form = AnimalForm(instance=animal)
        return render(request, 'milkfarm/edit/animal.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def update_labor(request, id):
    if request.user.is_authenticated:
        labor = Labor.objects.get(id=id)
        if request.method == 'POST':
            form = LaborForm(request.POST, instance=labor)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/labor.html',
                              {'form': form, 'message': 'Labor Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/labor.html', {'form': form, 'message': 'Labor Not Updated'})
        else:
            form = LaborForm(instance=labor)
        return render(request, 'milkfarm/edit/labor.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def update_expense(request, id):
    if request.user.is_authenticated:
        expense = Expense.objects.get(id=id)
        if request.method == 'POST':
            form = ExpenseForm(request.POST, instance=expense)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/expense.html',
                              {'form': form, 'message': 'Expense Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/expense.html', {'form': form, 'message': 'Expense Not Updated'})
        else:
            form = ExpenseForm(instance=expense)
        return render(request, 'milkfarm/edit/expense.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def update_grass(request, id):
    if request.user.is_authenticated:
        grass = Grass.objects.get(id=id)
        if request.method == 'POST':
            form = GrassForm(request.POST, instance=grass)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/grass.html',
                              {'form': form, 'message': 'Grass Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/grass.html', {'form': form, 'message': 'Grass Not Updated'})
        else:
            form = GrassForm(instance=grass)
        return render(request, 'milkfarm/edit/grass.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def home(request):
    return render(request, 'milkfarm/home.html')


def create_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerFormCreate(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/customer.html',
                              {'form': form, 'message': 'Customer Added Successfully'})
            else:
                return render(request, 'milkfarm/customer.html', {'form': form, 'message': 'Customer Not Added'})
        else:
            form = CustomerFormCreate()
        return render(request, 'milkfarm/customer.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_daily_delivery(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DailyDeliveryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/daily_delivery.html',
                              {'form': form, 'message': 'Daily Delivery Added Successfully'})
            else:
                return render(request, 'milkfarm/daily_delivery.html',
                              {'form': form, 'message': 'Daily Delivery Not Added'})
        else:
            form = DailyDeliveryForm()
        return render(request, 'milkfarm/daily_delivery.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_daily_production(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DailyProductionForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/daily_production.html',
                              {'form': form, 'message': 'Daily Production Added Successfully'})
            else:
                return render(request, 'milkfarm/daily_production.html',
                              {'form': form, 'message': 'Daily Production Not Added'})
        else:
            form = DailyProductionForm()
        return render(request, 'milkfarm/daily_production.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_payment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/payment.html',
                              {'form': form, 'message': 'Payment Added Successfully'})
            else:
                return render(request, 'milkfarm/payment.html', {'form': form, 'message': 'Payment Not Added'})
        else:
            form = PaymentForm()
        return render(request, 'milkfarm/payment.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def view_customer(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all()
        return render(request, 'milkfarm/display/customer.html', {'customers': customers})
    else:
        return render(request, 'users/not_loggedin.html')


def view_daily_delivery(request):
    if request.user.is_authenticated:
        daily_deliveries = DailyDelivery.objects.all()
        return render(request, 'milkfarm/display/daily_delivery.html', {'daily_deliveries': daily_deliveries})
    else:
        return render(request, 'users/not_loggedin.html')


def view_daily_production(request):
    if request.user.is_authenticated:
        daily_productions = DailyProduction.objects.all()
        return render(request, 'milkfarm/display/daily_production.html', {'daily_productions': daily_productions})
    else:
        return render(request, 'users/not_loggedin.html')


def view_payment(request):
    if request.user.is_authenticated:
        payments = Payment.objects.all()
        return render(request, 'milkfarm/display/payment.html', {'payments': payments})
    else:
        return render(request, 'users/not_loggedin.html')


def update_customer(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        if request.method == 'POST':
            form = CustomerFormUpdate(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/customer.html',
                              {'form': form, 'message': 'Customer Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/customer.html', {'form': form, 'message': 'Customer Not Updated'})
        else:
            form = CustomerFormUpdate(instance=customer)
        return render(request, 'milkfarm/edit/customer.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def update_payment(request, id):
    if request.user.is_authenticated:
        payment = Payment.objects.get(id=id)
        if request.method == 'POST':
            form = PaymentForm(request.POST, instance=payment)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/payment.html',
                              {'form': form, 'message': 'Payment Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/payment.html', {'form': form, 'message': 'Payment Not Updated'})
        else:
            form = PaymentForm(instance=payment)
        return render(request, 'milkfarm/edit/payment.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def update_daily_delivery(request, id):
    if request.user.is_authenticated:
        daily_delivery = DailyDelivery.objects.get(id=id)
        if request.method == 'POST':
            form = DailyDeliveryForm(request.POST, instance=daily_delivery)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/daily_delivery.html',
                              {'form': form, 'message': 'Daily Delivery Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/daily_delivery.html', {'form': form, 'message': 'Daily Delivery Not Updated'})
        else:
            form = DailyDeliveryForm(instance=daily_delivery)
        return render(request, 'milkfarm/edit/daily_delivery.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def update_daily_production(request, id):
    if request.user.is_authenticated:
        daily_production = DailyProduction.objects.get(id=id)
        if request.method == 'POST':
            form = DailyProductionForm(request.POST, instance=daily_production)
            if form.is_valid():
                form.save()
                return render(request, 'milkfarm/edit/daily_production.html',
                              {'form': form, 'message': 'Daily Production Updated Successfully'})
            else:
                return render(request, 'milkfarm/edit/daily_production.html', {'form': form, 'message': 'Daily Production Not Updated'})
        else:
            form = DailyProductionForm(instance=daily_production)
        return render(request, 'milkfarm/edit/daily_production.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_customer(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        customer.delete()
        return render(request, 'milkfarm/display/customer.html', {'message': 'Customer Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_daily_delivery(request, id):
    if request.user.is_authenticated:
        daily_delivery = DailyDelivery.objects.get(id=id)
        daily_delivery.delete()
        return render(request, 'milkfarm/display/daily_delivery.html', {'message': 'Daily Delivery Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_daily_production(request, id):
    if request.user.is_authenticated:
        daily_production = DailyProduction.objects.get(id=id)
        daily_production.delete()
        return render(request, 'milkfarm/display/daily_production.html', {'message': 'Daily Production Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_payment(request, id):
    if request.user.is_authenticated:
        payment = Payment.objects.get(id=id)
        payment.delete()
        return render(request, 'milkfarm/display/payment.html', {'message': 'Payment Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')