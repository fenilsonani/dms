from io import BytesIO

from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from .filters import CustomerFilter, DailyProductionFilter, DailyDeliveryFilter, AnimalFilter, LaborFilter, \
    ExpenseFilter, GrassFilter, PaymentFilter
from .forms import AnimalForm, LaborForm, ExpenseForm, GrassForm, CustomerFormCreate, DailyDeliveryForm, \
    DailyProductionForm, PaymentForm, CustomerFormUpdate
from .models import Animal, Labor, Expense, Grass, Customer, DailyDelivery, DailyProduction, Payment
from .resources import AnimalResource, LaborResource, ExpenseResource, GrassResource, CustomerResource, \
    DailyDeliveryResource, DailyProductionResource, PaymentResource


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
        animals = AnimalFilter(request.GET, queryset=Animal.objects.all())

        if 'export' in request.GET:
            dataset = AnimalResource().export(queryset=animals.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'milkfarm/display/animal.html', {'animals': animals})
    else:
        return render(request, 'users/not_loggedin.html')


def view_labor(request):
    if request.user.is_authenticated:
        labors = LaborFilter(request.GET, queryset=Labor.objects.all())

        if 'export' in request.GET:
            dataset = LaborResource().export(queryset=labors.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'milkfarm/display/labor.html', {'labors': labors})
    else:
        return render(request, 'users/not_loggedin.html')


def view_expense(request):
    if request.user.is_authenticated:
        expenses = ExpenseFilter(request.GET, queryset=Expense.objects.all())

        if 'export' in request.GET:
            dataset = ExpenseResource().export(queryset=expenses.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'milkfarm/display/expense.html', {'expenses': expenses})
    else:
        return render(request, 'users/not_loggedin.html')


def view_grass(request):
    if request.user.is_authenticated:
        grasses = GrassFilter(request.GET, queryset=Grass.objects.all())

        if 'export' in request.GET:
            dataset = GrassResource().export(queryset=grasses.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

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
                error = form.errors
                return render(request, 'milkfarm/daily_delivery.html',
                              {'form': form, 'message': 'Daily Delivery Not Added', 'error': error})
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
        customers = CustomerFilter(request.GET, queryset=Customer.objects.all())

        if 'export' in request.GET:
            dataset = CustomerResource().export(queryset=customers.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'milkfarm/display/customer.html', {'customers': customers})
    else:
        return render(request, 'users/not_loggedin.html')


def view_daily_delivery(request):
    if request.user.is_authenticated:
        daily_deliveries = DailyDeliveryFilter(request.GET, queryset=DailyDelivery.objects.all())

        if 'export' in request.GET:
            dataset = DailyDeliveryResource().export(queryset=daily_deliveries.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'milkfarm/display/daily_delivery.html', {'daily_deliveries': daily_deliveries})
    else:
        return render(request, 'users/not_loggedin.html')


def view_daily_production(request):
    if request.user.is_authenticated:
        daily_productions = DailyProductionFilter(request.GET, queryset=DailyProduction.objects.all())

        if 'export' in request.GET:
            dataset = DailyProductionResource().export(queryset=daily_productions.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'milkfarm/display/daily_production.html', {'daily_productions': daily_productions})
    else:
        return render(request, 'users/not_loggedin.html')


def view_payment(request):
    if request.user.is_authenticated:
        payments = PaymentFilter(request.GET, queryset=Payment.objects.all())

        if 'export' in request.GET:
            dataset = PaymentResource().export(queryset=payments.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

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
                return render(request, 'milkfarm/edit/daily_delivery.html',
                              {'form': form, 'message': 'Daily Delivery Not Updated'})
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
                return render(request, 'milkfarm/edit/daily_production.html',
                              {'form': form, 'message': 'Daily Production Not Updated'})
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
        return render(request, 'milkfarm/display/daily_delivery.html',
                      {'message': 'Daily Delivery Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_daily_production(request, id):
    if request.user.is_authenticated:
        daily_production = DailyProduction.objects.get(id=id)
        daily_production.delete()
        return render(request, 'milkfarm/display/daily_production.html',
                      {'message': 'Daily Production Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_payment(request, id):
    if request.user.is_authenticated:
        payment = Payment.objects.get(id=id)
        payment.delete()
        return render(request, 'milkfarm/display/payment.html', {'message': 'Payment Deleted Successfully'})
    else:
        return render(request, 'users/not_loggedin.html')


# create view for a generate bill page in that i will select the custom from the dropdown and then i will select the month and year and then i will click on the generate bill button then it will generate the bill for that month for a year
# in the bill it will show the customer name,address and mobile_number also for delivery it will show morning and evening milk for all the days of that month also show the sum of all delivery and also show the total amount for that month
# also show the total amount of grass for that month

def generate_bill(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            customer_id = request.POST['customer']
            month = request.POST['month']
            year = request.POST['year']

            customer = Customer.objects.get(id=customer_id)
            daily_deliveries = DailyDelivery.objects.filter(customer=customer, date__month=month, date__year=year)

            total_morning_milk = 0
            total_evening_milk = 0
            total_milk = 0
            total_amount = 0

            for delivery in daily_deliveries:
                total_morning_milk += delivery.morning_milk
                total_evening_milk += delivery.evening_milk
                daily_total = delivery.morning_milk + delivery.evening_milk
                total_milk += daily_total
                total_amount += daily_total * delivery.rate  # using the rate from DailyDelivery

            return render(request, 'milkfarm/bill.html',
                          {'customer': customer, 'daily_deliveries': daily_deliveries,
                           'total_morning_milk': total_morning_milk, 'total_evening_milk': total_evening_milk,
                           'total_milk': total_milk, 'total_amount': total_amount,
                           'month': month, 'year': year
                           })
        else:
            customers = Customer.objects.all()
            return render(request, 'milkfarm/generate_bill.html', {'customers': customers})


def download_bill(request, customer_id, month, year):
    # Fetch customer and daily deliveries
    customer = Customer.objects.get(id=customer_id)
    daily_deliveries = DailyDelivery.objects.filter(customer=customer, date__month=month, date__year=year)

    # Calculate totals
    total_morning_milk = sum(delivery.morning_milk for delivery in daily_deliveries)
    total_evening_milk = sum(delivery.evening_milk for delivery in daily_deliveries)
    total_amount = sum(delivery.total_milk * delivery.rate for delivery in daily_deliveries)

    # Initialize PDF generation
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()

    # Add customer details to PDF
    elements.append(Paragraph(f"Bill for {customer.name}", styles["Heading1"]))
    elements.append(Paragraph(f"Address: {customer.address}", styles["Normal"]))
    elements.append(Paragraph(f"Mobile Number: {customer.mobile_number}", styles["Normal"]))
    elements.append(Spacer(1, 0.25 * inch))

    # Create and style the table for deliveries
    table_data = [["Date", "Morning Milk", "Evening Milk", "Rate"]]
    for delivery in daily_deliveries:
        row = [str(delivery.date), str(delivery.morning_milk), str(delivery.evening_milk), str(delivery.rate)]
        table_data.append(row)

    table = Table(table_data, colWidths=[100, 100, 100, 100])
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)
    elements.append(table)

    # Add total amount to PDF
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(f"Total Amount: {total_amount}", styles["Normal"]))

    # Generate the PDF
    doc.build(elements)

    buffer.seek(0)
    return FileResponse(buffer, content_type='application/pdf', filename=f'bill_{customer_id}_{month}_{year}.pdf')
