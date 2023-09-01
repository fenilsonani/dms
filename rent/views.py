from django.shortcuts import render

from .forms import RentalPersonForm, RentPaymentForm, HouseForm
from .models import RentalPerson, House, RentPayment


# Create your views here.

def create_house(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HouseForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'rent/create_house.html',
                              {'form': form, 'message': 'House created successfully.'})
            else:
                return render(request, 'rent/create_house.html', {'form': form, 'message': 'House creation failed.'})
        else:
            form = HouseForm()
        return render(request, 'rent/create_house.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def create_rental(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RentalPersonForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'rent/create_rental.html',
                              {'form': form, 'message': 'Rental created successfully.'})
            else:
                return render(request, 'rent/create_rental.html', {'form': form, 'message': 'Rental creation failed.'})
        else:
            form = RentalPersonForm()
        return render(request, 'rent/create_rental.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def display_house(request):
    if request.user.is_authenticated:
        houses = House.objects.all()
        return render(request, 'rent/display/house.html', {'houses': houses})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def display_rental(request):
    if request.user.is_authenticated:
        rentals = RentalPerson.objects.all()
        return render(request, 'rent/display/rental.html', {'rentals': rentals})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def edit_house(request, id):
    if request.user.is_authenticated:
        house = House.objects.get(id=id)
        if request.method == 'POST':
            form = HouseForm(request.POST, instance=house)
            if form.is_valid():
                form.save()
                return render(request, 'rent/edit/house.html', {'form': form, 'message': 'House edited successfully.'})
            else:
                return render(request, 'rent/edit/house.html', {'form': form, 'message': 'House edit failed.'})
        else:
            form = HouseForm(instance=house)
            return render(request, 'rent/edit/house.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def edit_rental(request, id):
    if request.user.is_authenticated:
        rental = RentalPerson.objects.get(id=id)
        if request.method == 'POST':
            form = RentalPersonForm(request.POST, instance=rental)
            if form.is_valid():
                form.save()
                return render(request, 'rent/edit/rental.html',
                              {'form': form, 'message': 'Rental edited successfully.'})
            else:
                return render(request, 'rent/edit/rental.html', {'form': form, 'message': 'Rental edit failed.'})
        else:
            form = RentalPersonForm(instance=rental)
            return render(request, 'rent/edit/rental.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def delete_house(request, id):
    if request.user.is_authenticated:
        house = House.objects.get(id=id)
        house.delete()
        houses = House.objects.all()
        return render(request, 'rent/display/house.html', {'message': 'House deleted successfully.', 'houses': houses})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def delete_rental(request, id):
    if request.user.is_authenticated:
        rental = RentalPerson.objects.get(id=id)
        rental.delete()
        rentals = RentalPerson.objects.all()
        return render(request, 'rent/display/rental.html',
                      {'message': 'Rental deleted successfully.', 'rentals': rentals})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def add_rent_payment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RentPaymentForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'rent/add_rent_payment.html',
                              {'form': form, 'message': 'Rent payment added successfully.'})
            else:
                return render(request, 'rent/add_rent_payment.html',
                              {'form': form, 'message': 'Rent payment addition failed.'})
        else:
            form = RentPaymentForm()
            return render(request, 'rent/add_rent_payment.html', {'form': form})

    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def display_rent_payment(request):
    if request.user.is_authenticated:
        rent_payments = RentPayment.objects.all()
        return render(request, 'rent/display/rent_payment.html', {'rent_payments': rent_payments})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def edit_rent_payment(request, id):
    if request.user.is_authenticated:
        rent_payment = RentPayment.objects.get(id=id)
        if request.method == 'POST':
            form = RentPaymentForm(request.POST, instance=rent_payment)
            if form.is_valid():
                form.save()
                return render(request, 'rent/edit/rent_payment.html',
                              {'form': form, 'message': 'Rent payment edited successfully.'})
            else:
                return render(request, 'rent/edit/rent_payment.html',
                              {'form': form, 'message': 'Rent payment edit failed.'})
        else:
            form = RentPaymentForm(instance=rent_payment)
            return render(request, 'rent/edit/rent_payment.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})


def delete_rent_payment(request, id):
    if request.user.is_authenticated:
        rent_payment = RentPayment.objects.get(id=id)
        rent_payment.delete()
        rent_payments = RentPayment.objects.all()
        return render(request, 'rent/display/rent_payment.html',
                      {'message': 'Rent payment deleted successfully.', 'rent_payments': rent_payments})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})
