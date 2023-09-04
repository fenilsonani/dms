import csv

from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

from .forms import CustomerForm, DeliveryForm, Customer, Delivery


# Create your views here.


def create_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'rowater/customer.html',
                              {'form': form, 'message': 'Customer created successfully.'})
            else:
                return render(request, 'rowater/customer.html',
                              {'form': form, 'message': 'Customer creation failed.'})
        else:
            form = CustomerForm()
        return render(request, 'rowater/customer.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def create_delivery(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DeliveryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'rowater/delivery.html',
                              {'form': form, 'message': 'Delivery created successfully.'})
            else:
                error = form.errors
                return render(request, 'rowater/delivery.html',
                              {'form': form, 'message': 'Delivery creation failed.', 'error': error})
        else:
            form = DeliveryForm()
        return render(request, 'rowater/delivery.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def edit_customer(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        if request.method == 'POST':
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return render(request, 'rowater/edit/customer.html',
                              {'form': form, 'message': 'Customer edited successfully.'})
            else:
                return render(request, 'rowater/edit/customer.html',
                              {'form': form, 'message': 'Customer editing failed.'})
        else:
            form = CustomerForm(instance=customer)
        return render(request, 'rowater/edit/customer.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def edit_delivery(request, id):
    if request.user.is_authenticated:
        delivery = Delivery.objects.get(id=id)
        if request.method == 'POST':
            form = DeliveryForm(request.POST, instance=delivery)
            if form.is_valid():
                form.save()
                return render(request, 'rowater/edit/delivery.html',
                              {'form': form, 'message': 'Delivery edited successfully.'})
            else:
                return render(request, 'rowater/edit/delivery.html',
                              {'form': form, 'message': 'Delivery editing failed.'})
        else:
            form = DeliveryForm(instance=delivery)
        return render(request, 'rowater/edit/delivery.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def delete_customer(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        customer.delete()
        customers = Customer.objects.all()
        return render(request, 'rowater/display/customer.html', {'customers': customers})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def delete_delivery(request, id):
    if request.user.is_authenticated:
        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        deliveries = Delivery.objects.all()
        return render(request, 'rowater/display/delivery.html', {'deliveries': deliveries})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def display_delivery(request):
    if request.user.is_authenticated:
        deliveries = Delivery.objects.all()

        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf(deliveries)
            elif export_format == 'csv':
                response = generate_csv(deliveries)
            else:
                response = HttpResponse("Unsupported format")

            return response

        return render(request, 'icechip/display/delivery.html', {'deliveries': deliveries})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def generate_pdf(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="deliveries.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for delivery in data:
        pdf.drawString(100, 700, f'Delivery ID: {delivery.id}')
        pdf.drawString(100, 680, f'Delivery Date: {delivery.customer}')
        pdf.drawString(100, 660, f'Delivery Date: {delivery.date}')
        pdf.drawString(100, 640, f'Delivery Date: {delivery.daily_ice_block_given}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="deliveries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Delivery ID', 'Delivery Customer', 'Delivery Date', 'Delivery Ice Block Delivered',
                     'Delivery One Ice Chip Price', 'Delivery Total Ice Chip Price',
                     'Delivery Transportation Charge', 'Delivery Total Charge'])

    # Write your CSV content here
    for delivery in data:
        writer.writerow([delivery.id, delivery.customer, delivery.date, delivery.daily_ice_block_given,
                         delivery.one_ice_chip_price, delivery.total_ice_chip_price,
                         delivery.additional_transportation_charge, delivery.total_charge])

    return response


def display_customer(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all()

        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf1(customers)
            elif export_format == 'csv':
                response = generate_csv1(customers)
            else:
                response = HttpResponse("Unsupported format")

            return response

        return render(request, 'icechip/display/customer.html', {'customers': customers})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def generate_pdf1(data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="customers.pdf"'

    pdf = canvas.Canvas(response)

    # Define your PDF layout and content here
    for customer in data:
        pdf.drawString(100, 700, f'Customer ID: {customer.id}')
        pdf.drawString(100, 680, f'Customer Name: {customer.name}')
        pdf.drawString(100, 660, f'Customer Address: {customer.address}')
        pdf.drawString(100, 640, f'Customer Phone Number: {customer.phone_number}')
        pdf.drawString(100, 620, f'Customer Paid Amount: {customer.paid_amount}')
        pdf.drawString(100, 600, f'Customer Pending Amount: {customer.pending_amount}')
        pdf.showPage()

    pdf.save()
    return response


def generate_csv1(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customers.csv"'

    writer = csv.writer(response)
    writer.writerow(['Customer ID', 'Customer Name', 'Customer Address', 'Customer Phone Number',
                     'Customer Paid Amount', 'Customer Pending Amount'])

    # Write your CSV content here
    for customer in data:
        writer.writerow([customer.id, customer.name, customer.address, customer.phone_number,
                         customer.paid_amount, customer.pending_amount])

    return response
