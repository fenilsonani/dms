import csv

from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

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


def generate_pdf(animals):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for animal in animals:
        pdf.drawString(100, 700, f'Labor ID: {animal.id}')
        pdf.drawString(100, 680, f'Labor Date: {animal.name}')
        pdf.drawString(100, 660, f'Labor Date: {animal.location}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv(animals):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Animal Id', 'Animal Name', 'Animal Location'])

    # Write your CSV content here
    for animal in animals:
        writer.writerow([animal.id, animal.name, animal.location])

    return response


def generate_pdf1(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for dt in data:
        pdf.drawString(100, 700, f'Labor ID: {dt.id}')
        pdf.drawString(100, 680, f'Labor Nmae: {dt.name}')
        pdf.drawString(100, 660, f'Labor Mobile No: {dt.mobile_number}')
        pdf.drawString(100, 660, f'Labor Labor type: {dt.labor_type}')
        pdf.drawString(100, 660, f'Labor Payment To Be Paid: {dt.payment_to_be_paid}')
        pdf.drawString(100, 660, f'Labor Credit: {dt.credit}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv1(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Animal Id', 'Animal Name', 'Animal Mobile No', 'Animal Labor Type', 'Labor Pyament To Be Paid',
                     'Labor Credit'])

    # Write your CSV content here
    for dt in data:
        writer.writerow([dt.id, dt.name, dt.mobile_number, dt.labor_type, dt.payment_to_be_paid, dt.credit])

    return response


def generate_pdf2(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for dt in data:
        pdf.drawString(100, 700, f'Expense ID: {dt.id}')
        pdf.drawString(100, 680, f'Expense Type: {dt.expenses_type}')
        pdf.drawString(100, 660, f'Expense Amount: {dt.amount}')
        pdf.drawString(100, 660, f'Expense Date: {dt.date}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv2(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Expense Id', 'Expense Type', 'Expense Amount', 'Expense Date'])

    # Write your CSV content here
    for dt in data:
        writer.writerow([dt.id, dt.expenses_type, dt.amount, dt.date])

    return response


def generate_pdf3(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for dt in data:
        pdf.drawString(100, 700, f'Grass ID: {dt.id}')
        pdf.drawString(100, 680, f'Grass Location: {dt.location}')
        pdf.drawString(100, 660, f'Grass Owner Name: {dt.owner_name}')
        pdf.drawString(100, 660, f'Grass Owner Mobile: {dt.owner_mobile}')
        pdf.drawString(100, 660, f'Grass Total Amount Grass: {dt.total_amount_grass}')
        pdf.drawString(100, 660, f'Grass Rate: {dt.rate}')
        pdf.drawString(100, 660, f'Grass Final Price: {dt.final_price}')
        pdf.drawString(100, 660, f'Grass Due Amount: {dt.due_amount}')
        pdf.drawString(100, 660, f'Grass Amount To Be Paid: {dt.amount_to_be_paid}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv3(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Grass Id', 'Grass Location', 'Grass Owner Name', 'Grass Owner Mobile', 'Grass Total Amount Grass',
                     'Grass Rate', 'Grass Final Price', 'Grass Due Amount', 'Grass Amount To Be Paid'])

    # Write your CSV content here
    for dt in data:
        writer.writerow([dt.id, dt.location, dt.owner_name, dt.owner_mobile, dt.total_amount_grass, dt.rate,
                         dt.final_price, dt.due_amount, dt.amount_to_be_paid])

    return response


def view_animal(request):
    if request.user.is_authenticated:
        animals = Animal.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf(animals)
            elif export_format == 'csv':
                response = generate_csv(animals)
            else:
                response = HttpResponse("Unsupported format")

            return response
        return render(request, 'milkfarm/display/animal.html', {'animals': animals})
    else:
        return render(request, 'users/not_loggedin.html')


def view_labor(request):
    if request.user.is_authenticated:
        labors = Labor.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf1(labors)
            elif export_format == 'csv':
                response = generate_csv1(labors)
            else:
                response = HttpResponse("Unsupported format")

            return response
        return render(request, 'milkfarm/display/labor.html', {'labors': labors})
    else:
        return render(request, 'users/not_loggedin.html')


def view_expense(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf2(expenses)
            elif export_format == 'csv':
                response = generate_csv2(expenses)
            else:
                response = HttpResponse("Unsupported format")

            return response
        return render(request, 'milkfarm/display/expense.html', {'expenses': expenses})
    else:
        return render(request, 'users/not_loggedin.html')


def view_grass(request):
    if request.user.is_authenticated:
        grasses = Grass.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf3(grasses)
            elif export_format == 'csv':
                response = generate_csv3(grasses)
            else:
                response = HttpResponse("Unsupported format")

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
        customers = Customer.objects.all()
        return render(request, 'milkfarm/display/customer.html', {'customers': customers})
    else:
        return render(request, 'users/not_loggedin.html')


def generate_pdf4(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for dt in data:
        pdf.drawString(100, 700, f'Daily Delivery ID: {dt.id}')
        pdf.drawString(100, 680, f'Daily Delivery Customer: {dt.customer}')
        pdf.drawString(100, 660, f'Daily Delivery Date: {dt.date}')
        pdf.drawString(100, 660, f'Daily Delivery Morning Milk: {dt.morning_milk}')
        pdf.drawString(100, 660, f'Daily Delivery Evening Milk: {dt.evening_milk}')
        pdf.drawString(100, 660, f'Daily Delivery Total Milk: {dt.total_milk}')
        pdf.drawString(100, 660, f'Daily Delivery Rate: {dt.rate}')
        pdf.drawString(100, 660, f'Daily Delivery Final Price: {dt.final_price}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv4(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Daily Delivery Id', 'Daily Delivery Customer', 'Daily Delivery Date', 'Daily Delivery Morning Milk',
         'Daily Delivery Evening Milk', 'Daily Delivery Total Milk', 'Daily Delivery Rate',
         'Daily Delivery Final Price'])

    # Write your CSV content here
    for dt in data:
        writer.writerow([dt.id, dt.customer, dt.date, dt.morning_milk, dt.evening_milk, dt.total_milk, dt.rate,
                         dt.final_price])

    return response


def view_daily_delivery(request):
    if request.user.is_authenticated:
        daily_deliveries = DailyDelivery.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf4(daily_deliveries)
            elif export_format == 'csv':
                response = generate_csv4(daily_deliveries)
            else:
                response = HttpResponse("Unsupported format")

            return response
        return render(request, 'milkfarm/display/daily_delivery.html', {'daily_deliveries': daily_deliveries})
    else:
        return render(request, 'users/not_loggedin.html')


def generate_pdf5(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for dt in data:
        pdf.drawString(100, 700, f'Daily Production ID: {dt.id}')
        pdf.drawString(100, 680, f'Daily Production Date: {dt.date}')
        pdf.drawString(100, 660, f'Daily Production Milk: {dt.milk}')
        pdf.drawString(100, 660, f'Daily Production Rate: {dt.rate}')
        pdf.drawString(100, 660, f'Daily Production Final Price: {dt.final_price}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv5(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Daily Production Id', 'Daily Production Date', 'Daily Production Milk', 'Daily Production Rate',
         'Daily Production Final Price'])

    # Write your CSV content here
    for dt in data:
        writer.writerow([dt.id, dt.date, dt.milk, dt.rate, dt.final_price])

    return response


def view_daily_production(request):
    if request.user.is_authenticated:
        daily_productions = DailyProduction.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf5(daily_productions)
            elif export_format == 'csv':
                response = generate_csv5(daily_productions)
            else:
                response = HttpResponse("Unsupported format")

            return response
        return render(request, 'milkfarm/display/daily_production.html', {'daily_productions': daily_productions})
    else:
        return render(request, 'users/not_loggedin.html')

def generate_pdf6(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for dt in data:
        pdf.drawString(100, 700, f'Payment ID: {dt.id}')
        pdf.drawString(100, 680, f'Payment Customer: {dt.customer}')
        pdf.drawString(100, 660, f'Payment Date: {dt.date}')
        pdf.drawString(100, 660, f'Payment Amount: {dt.amount}')
        pdf.drawString(100, 660, f'Payment Payment Type: {dt.payment_type}')
        pdf.drawString(100, 660, f'Payment Payment To Be Paid: {dt.payment_to_be_paid}')
        pdf.drawString(100, 660, f'Payment Credit: {dt.credit}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv6(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Payment Id', 'Payment Customer', 'Payment Date', 'Payment Amount', 'Payment Payment Type',
         'Payment Payment To Be Paid', 'Payment Credit'])

    # Write your CSV content here
    for dt in data:
        writer.writerow([dt.id, dt.customer, dt.date, dt.amount, dt.payment_type, dt.payment_to_be_paid, dt.credit])

    return response

def view_payment(request):
    if request.user.is_authenticated:
        payments = Payment.objects.all()
        if request.method=='POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf6(payments)
            elif export_format == 'csv':
                response = generate_csv6(payments)
            else:
                response = HttpResponse("Unsupported format")

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
