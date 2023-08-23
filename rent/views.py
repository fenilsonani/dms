from django.shortcuts import render

from .forms import RentalForm, HouseForm
from .models import Rental, House


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
            form = RentalForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'rent/create_rental.html',
                              {'form': form, 'message': 'Rental created successfully.'})
            else:
                return render(request, 'rent/create_rental.html', {'form': form, 'message': 'Rental creation failed.'})
        else:
            form = RentalForm()
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
        rentals = Rental.objects.all()
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
        rental = Rental.objects.get(id=id)
        if request.method == 'POST':
            form = RentalForm(request.POST, instance=rental)
            if form.is_valid():
                form.save()
                return render(request, 'rent/edit/rental.html',
                              {'form': form, 'message': 'Rental edited successfully.'})
            else:
                return render(request, 'rent/edit/rental.html', {'form': form, 'message': 'Rental edit failed.'})
        else:
            form = RentalForm(instance=rental)
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
        rental = Rental.objects.get(id=id)
        rental.delete()
        rentals = Rental.objects.all()
        return render(request, 'rent/display/rental.html',
                      {'message': 'Rental deleted successfully.', 'rentals': rentals})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})