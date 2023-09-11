import csv
import io

from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

from .forms import FarmForm, SeasonForm, CropForm, ExpenseForm, SeasonExpenseForm
from .models import Farm, Season, Crop, Expense, SeasonExpense


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
        crops = Crop.objects.all()

        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf1(crops)
            elif export_format == 'csv':
                response = generate_csv1(crops)
            else:
                response = HttpResponse("Unsupported format")

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
        seasons = Season.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf3(seasons)
            elif export_format == 'csv':
                response = generate_csv3(seasons)
            else:
                response = HttpResponse("Unsupported format")

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
        season_expenses = SeasonExpense.objects.all()
        if request.method == 'POST':
            print(request.POST)
            export_format = request.POST.get('export_format')
            if export_format == 'pdf':
                response = generate_pdf4(season_expenses)
            elif export_format == 'csv':
                response = generate_csv4(season_expenses)
            else:
                response = HttpResponse("Unsupported format")

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
        farms = Farm.objects.all()
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


def generate_pdf1(crops):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 10 * inch, "Crops")
    data = []
    data.append(['Name'])
    for crop in crops:
        data.append([crop.name])
    t = Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.green)]))
    t.wrapOn(p, 0, 0)
    t.drawOn(p, 1 * inch, 9 * inch)
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


def generate_csv1(crops):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="crops.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name'])
    for crop in crops:
        writer.writerow([crop.name])
    return response


def generate_pdf2(expenses):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 10 * inch, "Expenses")
    data = []
    data.append(['Name'])
    for expense in expenses:
        data.append([expense.name])
    t = Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.green)]))
    t.wrapOn(p, 0, 0)
    t.drawOn(p, 1 * inch, 9 * inch)
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


def generate_csv2(expenses):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name'])
    for expense in expenses:
        writer.writerow([expense.name])
    return response


def generate_pdf3(seasons):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 10 * inch, "Seasons")
    data = []
    data.append(['Farm', 'Crop', 'Starting Date', 'Harvested Crop Amount (Tons)', 'Harvested Crop Price Per Ton',
                 'First Payment', 'Second Payment', 'Status'])
    for season in seasons:
        data.append([season.farm.name, season.crop.name, season.starting_date, season.harvested_crop_amount_tons,
                     season.harvested_crop_price_per_ton, season.first_payment, season.second_payment, season.status])
    t = Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.green)]))
    t.wrapOn(p, 0, 0)
    t.drawOn(p, 1 * inch, 9 * inch)
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


def generate_csv3(seasons):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="seasons.csv"'
    writer = csv.writer(response)
    writer.writerow(['Farm', 'Crop', 'Starting Date', 'Harvested Crop Amount (Tons)', 'Harvested Crop Price Per Ton',
                     'First Payment', 'Second Payment', 'Status'])
    for season in seasons:
        writer.writerow([season.farm.name, season.crop.name, season.starting_date, season.harvested_crop_amount_tons,
                         season.harvested_crop_price_per_ton, season.first_payment, season.second_payment,
                         season.status])
    return response


def generate_pdf4(season_expenses):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 10 * inch, "Season Expenses")
    data = []
    data.append(['Season', 'Expense', 'Amount'])
    for season_expense in season_expenses:
        data.append([season_expense.season, season_expense.expense, season_expense.amount])
    t = Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.green)]))
    t.wrapOn(p, 0, 0)
    t.drawOn(p, 1 * inch, 9 * inch)
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


def generate_csv4(season_expenses):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="season_expenses.csv"'
    writer = csv.writer(response)
    writer.writerow(['Season', 'Expense', 'Amount'])
    for season_expense in season_expenses:
        writer.writerow([season_expense.season, season_expense.expense, season_expense.amount])
    return response
