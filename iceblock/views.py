from django.shortcuts import render
from .forms import CustomerForm, DeliveryForm
from .models import Customer, Delivery
# Create your views here.
def create_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'iceblock/create_customer.html', {'form': form,'message': 'Customer created successfully.'})
            else:
                return render(request, 'iceblock/create_customer.html', {'form': form,'message': 'Customer creation failed.'})
        else:
            form = CustomerForm()
        return render(request, 'iceblock/create_customer.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})

def create_delivery(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DeliveryForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'iceblock/create_delivery.html', {'form': form,'message': 'Delivery created successfully.'})
            else:
                return render(request, 'iceblock/create_delivery.html', {'form': form,'message': 'Delivery creation failed.'})
        else:
            form = DeliveryForm()
        return render(request, 'iceblock/create_delivery.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})

def display_customer(request):
    if request.user.is_authenticated:
        customers = Customer.objects.all()
        return render(request, 'iceblock/display/customer.html', {'customers': customers})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})

def display_delivery(request):
    if request.user.is_authenticated:
        deliveries = Delivery.objects.all()
        return render(request, 'iceblock/display/delivery.html', {'deliveries': deliveries})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})

def edit_customer(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        if request.method == 'POST':
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return render(request, 'iceblock/edit/customer.html', {'form': form,'message': 'Customer edited successfully.'})
            else:
                return render(request, 'iceblock/edit/customer.html', {'form': form,'message': 'Customer edit failed.'})
        else:
            form = CustomerForm(instance=customer)
        return render(request, 'iceblock/edit/customer.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})

def edit_delivery(request, id):
    if request.user.is_authenticated:
        delivery = Delivery.objects.get(id=id)
        if request.method == 'POST':
            form = DeliveryForm(request.POST, instance=delivery)
            if form.is_valid():
                form.save()
                return render(request, 'iceblock/edit/delivery.html', {'form': form,'message': 'Delivery edited successfully.'})
            else:
                return render(request, 'iceblock/edit/delivery.html', {'form': form,'message': 'Delivery edit failed.'})
        else:
            form = DeliveryForm(instance=delivery)
        return render(request, 'iceblock/edit/delivery.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})

def delete_customer(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        customer.delete()
        customers = Customer.objects.all()
        return render(request, 'iceblock/display/customer.html', {'customers': customers})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})

def delete_delivery(request, id):
    if request.user.is_authenticated:
        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        deliveries = Delivery.objects.all()
        return render(request, 'iceblock/display/delivery.html', {'deliveries': deliveries})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})