from django.http import HttpResponse
from django.shortcuts import render

from .filters import FarmFilter, SeasonFilter, SeasonExpenseFilter, ExpenseFilter, CropFilter
from .forms import FarmForm, SeasonForm, CropForm, ExpenseForm, SeasonExpenseForm
from .models import Farm, Season, Crop, Expense, SeasonExpense
from .resources import SeasonExpenseResource, CropResource, FarmResource, SeasonResource, ExpenseResource


# Create your views here.
def create_crop(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CropForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'farm/add_crop.html', {'form': form, 'message': 'Crop added successfully'})
            else:
                return render(request, 'farm/add_crop.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = CropForm()
            return render(request, 'farm/add_crop.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_expense_type(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'farm/add_expense_type.html',
                              {'form': form, 'message': 'Expense added successfully'})
            else:
                return render(request, 'farm/add_expense_type.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = ExpenseForm()
            return render(request, 'farm/add_expense_type.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_season(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SeasonForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'farm/add_season.html', {'form': form, 'message': 'Season added successfully'})
            else:
                error = form.errors
                return render(request, 'farm/add_season.html',
                              {'form': form, 'message': 'Invalid form', 'error': error})
        else:
            form = SeasonForm()
            return render(request, 'farm/add_season.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_season_expense(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SeasonExpenseForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'farm/add_expense.html',
                              {'form': form, 'message': 'Season Expense added successfully'})
            else:
                return render(request, 'farm/add_expense.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = SeasonExpenseForm()
            return render(request, 'farm/add_expense.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def create_farm(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FarmForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'farm/add_farm.html', {'form': form, 'message': 'Farm added successfully'})
            else:
                return render(request, 'farm/add_farm.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = FarmForm()
            return render(request, 'farm/add_farm.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def display_crop(request):
    if request.user.is_authenticated:
        crops = CropFilter(request.GET, queryset=Crop.objects.all())

        if 'export' in request.GET:
            dataset = CropResource().export(queryset=crops.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'farm/display/display_crop.html', {'crops': crops})
    else:
        return render(request, 'users/not_loggedin.html')


def edit_crop(request, id):
    if request.user.is_authenticated:
        crop = Crop.objects.get(pk=id)
        if request.method == 'POST':
            form = CropForm(request.POST, instance=crop)
            if form.is_valid():
                form.save()
                return render(request, 'farm/edit/edit_crop.html',
                              {'form': form, 'message': 'Crop updated successfully'})
            else:
                return render(request, 'farm/edit/edit_crop.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = CropForm(instance=crop)
            return render(request, 'farm/edit/edit_crop.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_crop(request, id):
    if request.user.is_authenticated:
        crop = Crop.objects.get(pk=id)
        crop.delete()
        crops = Crop.objects.all()
        return render(request, 'farm/display/display_crop.html',
                      {'message': 'Crop deleted successfully', 'crops': crops})
    else:
        return render(request, 'users/not_loggedin.html')


def display_expense_type(request):
    if request.user.is_authenticated:
        expenses = ExpenseFilter(request.GET, queryset=Expense.objects.all())
        if 'export' in request.GET:
            dataset = ExpenseResource().export(queryset=expenses.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response
        return render(request, 'farm/display/display_expense_type.html', {'expenses': expenses})
    else:
        return render(request, 'users/not_loggedin.html')


def edit_expense_type(request, id):
    if request.user.is_authenticated:
        expense = Expense.objects.get(pk=id)
        if request.method == 'POST':
            form = ExpenseForm(request.POST, instance=expense)
            if form.is_valid():
                form.save()
                return render(request, 'farm/edit/edit_expense_type.html',
                              {'form': form, 'message': 'Expense updated successfully'})
            else:
                return render(request, 'farm/edit/edit_expense_type.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = ExpenseForm(instance=expense)
            return render(request, 'farm/edit/edit_expense_type.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_expense_type(request, id):
    if request.user.is_authenticated:
        expense = Expense.objects.get(pk=id)
        expense.delete()
        expenses = Expense.objects.all()
        return render(request, 'farm/display/display_expense_type.html',
                      {'message': 'Expense deleted successfully', 'expenses': expenses})
    else:
        return render(request, 'users/not_loggedin.html')


def display_season(request):
    if request.user.is_authenticated:
        seasons = SeasonFilter(request.GET, queryset=Season.objects.all())

        if 'export' in request.GET:
            dataset = SeasonResource().export(queryset=seasons.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'farm/display/display_season.html', {'seasons': seasons})
    else:
        return render(request, 'users/not_loggedin.html')


def edit_season(request, id):
    if request.user.is_authenticated:
        season = Season.objects.get(pk=id)
        if request.method == 'POST':
            form = SeasonForm(request.POST, instance=season)
            if form.is_valid():
                form.save()
                return render(request, 'farm/edit/edit_season.html',
                              {'form': form, 'message': 'Season updated successfully'})
            else:
                return render(request, 'farm/edit/edit_season.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = SeasonForm(instance=season)
            return render(request, 'farm/edit/edit_season.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_season(request, id):
    if request.user.is_authenticated:
        season = Season.objects.get(pk=id)
        season.delete()
        seasons = Season.objects.all()
        return render(request, 'farm/display/display_season.html',
                      {'message': 'Season deleted successfully', 'seasons': seasons})
    else:
        return render(request, 'users/not_loggedin.html')


def display_season_expense(request):
    if request.user.is_authenticated:
        season_expenses = SeasonExpenseFilter(request.GET, queryset=SeasonExpense.objects.all())

        if 'export' in request.GET:
            dataset = SeasonExpenseResource().export(queryset=season_expenses.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'farm/display/display_season_expense.html', {'season_expenses': season_expenses})
    else:
        return render(request, 'users/not_loggedin.html')


def edit_season_expense(request, id):
    if request.user.is_authenticated:
        season_expense = SeasonExpense.objects.get(pk=id)
        if request.method == 'POST':
            form = SeasonExpenseForm(request.POST, instance=season_expense)
            if form.is_valid():
                form.save()
                return render(request, 'farm/edit/edit_season_expense.html',
                              {'form': form, 'message': 'Season Expense updated successfully'})
            else:
                return render(request, 'farm/edit/edit_season_expense.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = SeasonExpenseForm(instance=season_expense)
            return render(request, 'farm/edit/edit_season_expense.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_season_expense(request, id):
    if request.user.is_authenticated:
        season_expense = SeasonExpense.objects.get(pk=id)
        season_expense.delete()
        season_expenses = SeasonExpense.objects.all()
        return render(request, 'farm/display/display_season_expense.html',
                      {'message': 'Season Expense deleted successfully', 'season_expenses': season_expenses})
    else:
        return render(request, 'users/not_loggedin.html')


def display_farm(request):
    if request.user.is_authenticated:
        farms = FarmFilter(request.GET, queryset=Farm.objects.all())

        if 'export' in request.GET:
            dataset = FarmResource().export(queryset=farms.qs)
            response = HttpResponse(dataset.csv, content_type='text/csv')
            return response

        return render(request, 'farm/display/display_farm.html', {'farms': farms})
    else:
        return render(request, 'users/not_loggedin.html')


def edit_farm(request, id):
    if request.user.is_authenticated:
        farm = Farm.objects.get(pk=id)
        if request.method == 'POST':
            form = FarmForm(request.POST, instance=farm)
            if form.is_valid():
                form.save()
                return render(request, 'farm/edit/edit_farm.html',
                              {'form': form, 'message': 'Farm updated successfully'})
            else:
                return render(request, 'farm/edit/edit_farm.html', {'form': form, 'message': 'Invalid form'})
        else:
            form = FarmForm(instance=farm)
            return render(request, 'farm/edit/edit_farm.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html')


def delete_farm(request, id):
    if request.user.is_authenticated:
        farm = Farm.objects.get(pk=id)
        farm.delete()
        farms = Farm.objects.all()
        return render(request, 'farm/display/display_farm.html',
                      {'message': 'Farm deleted successfully', 'farms': farms})
    else:
        return render(request, 'users/not_loggedin.html')
