import datetime
from collections import defaultdict

from django.shortcuts import render

from milkfarm.models import Customer, Labor, Animal
from milkfarm.models import DailyProduction, Expense
from users.forms import NormalUserForm, RegisterForm
from users.is_admin import is_admin
from users.models import NormalUser, Business
from rent.models import House,RentPayment,RentalPerson


# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        final = is_admin(request.user)  # You mentioned you have this function
        if final:
            # find the bussiness type and pass it to the template
            business = Business.objects.get(admin=request.user)
            # pass the user of the business to the template
            users = NormalUser.objects.filter(business=business)

            business = business.name.lower()

            if business == "farming":
                return render(request, 'dashboard/admin_dash.html',
                              {'usertype': 'Admin', 'business': business, 'users': users})
            elif business == "milk":
                customer_length = len(Customer.objects.all())
                emp_length = len(users)
                labor_length = len(Labor.objects.all())
                animal_length = len(Animal.objects.all())
                # get only recent 7 days data of milk production
                chart_data = DailyProduction.objects.all().order_by('-date')[:7]
                chart_label = [(entry.date.strftime('%Y-%m-%d'), float(entry.total_milk)) for entry in chart_data][::-1]
                chart_data = [float(entry.total_milk) for entry in chart_data][::-1]
                chart_data = str(chart_data)
                today = datetime.date.today()
                current_month = today.month
                current_year = today.year

                # Retrieve expenses for the current month
                current_month_expenses = Expense.objects.filter(date__month=current_month, date__year=current_year)

                # Calculate total expenses for each type
                expenses_by_type = defaultdict(float)
                for expense in current_month_expenses:
                    expenses_by_type[expense.expenses_type] += float(expense.amount)

                # Prepare data for the pie chart
                pie_labels = list(expenses_by_type.keys())
                pie_data = list(expenses_by_type.values())

                current_year_expenses = Expense.objects.filter(date__year=current_year)

                # Calculate total expenses for each month
                expenses_by_month = defaultdict(float)
                for expense in current_year_expenses:
                    expenses_by_month[expense.date.month] += float(expense.amount)

                # Prepare data for the line chart
                line_labels = [datetime.date(current_year, month, 1).strftime('%B') for month in range(1, 13)]
                line_data = [expenses_by_month.get(month, 0) for month in range(1, 13)]

                return render(request, 'dashboard/admin_dash_milk.html',
                              {'usertype': 'Admin', 'business': business, 'users': users,
                               'customer_length': customer_length, 'emp_length': emp_length,
                               'labor_length': labor_length, 'animal_length': animal_length,
                               'chart_label': chart_label,
                               'pie_labels': pie_labels,
                               'line_labels': line_labels,
                               'line_data': line_data,
                               'pie_data': pie_data,
                               'chart_data': chart_data})
            elif business == "transport":
                return render(request, 'dashboard/admin_dash_transport.html',
                              {'usertype': 'Admin', 'business': business, 'users': users})
            elif business == "iceblock":
                return render(request, 'dashboard/admin_dash_iceb.html',
                              {'usertype': 'Admin', 'business': business, 'users': users})
            elif business == "rent":
                house_length=len(House.objects.all())

                return render(request, 'dashboard/admin_dash_rent.html',
                              {'usertype': 'Admin', 'business': business, 'users': users,
                               })
            else:
                return render(request, 'dashboard/admin_dash.html',
                              {'usertype': 'Admin', 'business': business, 'users': users})
        else:
            return render(request, 'dashboard/normal_dash.html', {'usertype': 'Normal'})
    else:
        return render(request, 'users/not_loggedin.html')


def add_user_into_system(request):
    if request.user.is_authenticated:
        final = is_admin(request.user)  # You mentioned you have this function
        if final:
            if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    user.refresh_from_db()
                    user.save()
                    message = "User added successfully"
                    form = RegisterForm()
                    return render(request, 'dashboard/add_user.html', {'form': form, 'message': message})
                else:
                    error = form.errors
                    form = RegisterForm()
                    message = "Invalid form"
                    return render(request, 'dashboard/add_user.html',
                                  {'form': form, 'error': error, 'message': message})
            else:
                form = RegisterForm()
                return render(request, 'dashboard/add_user.html', {'form': form})
        else:
            return render(request, 'dashboard/normal_dash.html', {'message': 'You are not an admin'})
    else:
        return render(request, 'users/not_loggedin.html')


def add_normal_user(request):
    if request.user.is_authenticated:
        final = is_admin(request.user)  # You mentioned you have this function
        if final:
            if request.method == 'POST':
                form = NormalUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    message = "User added successfully"
                    form = NormalUserForm()
                    return render(request, 'dashboard/add_normal.html', {'form': form, 'message': message})
                else:
                    error = form.errors
                    return render(request, 'dashboard/add_normal.html', {'form': form, 'error': error})
            else:
                form = NormalUserForm()
                return render(request, 'dashboard/add_normal.html', {'form': form})
        else:
            return render(request, 'dashboard/normal_dash.html', {'message': 'You are not an admin'})
    else:
        return render(request, 'users/not_loggedin.html')
