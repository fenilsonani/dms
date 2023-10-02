import datetime
from collections import defaultdict
from datetime import date, timedelta

from django.db.models import Sum, Count
from django.shortcuts import render, redirect

from farm.models import Farm, Season, SeasonExpense, Crop
from iceblock.models import Customer as IceCustomer
from iceblock.models import Delivery as IceDelivery
from icechip.models import Customer as IceChipCustomer
from icechip.models import Delivery as IceChipDelivery
from milkfarm.models import Customer, Labor, Animal
from milkfarm.models import DailyProduction, Expense
from rent.models import House, RentPayment, RentalPerson
from rowater.models import Customer as RowaterCustomer
from rowater.models import Delivery as RowaterDelivery
from transport.models import Expense as transportExpense
from transport.models import TransportExpenses, Trips
from users.forms import NormalUserForm, RegisterForm
from users.is_admin import is_admin
from users.models import NormalUser, Business


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
                emp_length = len(users.all())
                farm_length = len(Farm.objects.all())
                season_length = len(Season.objects.all())
                crop_length = len(Crop.objects.all())
                expense_length = len(Expense.objects.all())
                season_expense_length = len(SeasonExpense.objects.all())
                seasons = Season.objects.all()

                # Data for harvested crop amount chart
                harvested_crop_amounts = [season.harvested_crop_amount_tons for season in seasons]

                # Data for expenses chart
                expense_categories = Season.EXPENSE_CHOICES
                expense_data = {}

                for category, _ in expense_categories:
                    expense_data[category] = []

                for category, _ in expense_categories:
                    for season in seasons:
                        total_expense = \
                            season.seasonexpense_set.filter(expense__name=category).aggregate(total=Sum('amount'))[
                                'total'] or 0
                        expense_data[category].append(total_expense)
                print(expense_data)
                contex = {
                    'usertype': 'Admin', 'business': business,
                    'emp_length': emp_length, 'farm_length': farm_length,
                    'season_length': season_length, 'crop_length': crop_length,
                    'expense_length': expense_length, 'season_expense_length': season_expense_length,
                    'seasons': seasons,
                    'harvested_crop_amounts': harvested_crop_amounts,
                    'expense_categories': expense_categories,
                    'expense_data': expense_data,
                }
                return render(request, 'dashboard/admin_dash_farm.html',
                              contex)
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
                              {'usertype': 'Admin', 'business': business,
                               'customer_length': customer_length, 'emp_length': emp_length,
                               'labor_length': labor_length, 'animal_length': animal_length,
                               'chart_label': chart_label,
                               'pie_labels': pie_labels,
                               'line_labels': line_labels,
                               'line_data': line_data,
                               'pie_data': pie_data,
                               'chart_data': chart_data})
            elif business == "transport":
                emp_length = len(users.all())
                expense_length = len(transportExpense.objects.all())
                trips_length = len(Trips.objects.all())
                expense_type_length = len(TransportExpenses.objects.all())

                expenses = TransportExpenses.objects.all()
                expenses_grouped = TransportExpenses.objects.values('date').annotate(
                    total_amount=Sum('amount')).order_by('date')
                trips_count = Trips.objects.values('date').annotate(num_trips=Count('id')).order_by('date')
                return render(request, 'dashboard/admin_dash_transport.html',
                              {'usertype': 'Admin', 'business': business,
                               'expense_type_length': expense_type_length, 'expense_length': expense_length,
                               'trips_length': trips_length, 'emp_length': emp_length,
                               'expenses': expenses, 'expenses_grouped': expenses_grouped,
                               'trips_count': trips_count
                               })

            elif business == "iceblock":
                one_week_ago = date.today() - timedelta(days=7)
                customer_length = len(IceCustomer.objects.all())
                emp_length = len(users.all())
                total_delivery = len(IceDelivery.objects.all())
                delivery_data = (
                    IceDelivery.objects
                    .filter(date__gte=one_week_ago)
                    .values('date')
                    .annotate(total_deliveries=Count('id'))
                    .order_by('date')
                )
                labels = [str(item['date']) for item in delivery_data]
                data = [item['total_deliveries'] for item in delivery_data]

                delivery_data1 = (
                    IceDelivery.objects
                    .filter(date__gte=one_week_ago)  # Filter data for the last 7 days
                    .values('date')
                    .annotate(total_ice_blocks=Sum('daily_ice_block_given'))
                    .order_by('date')
                )

                labels1 = [str(item['date']) for item in delivery_data1]
                data1 = [item['total_ice_blocks'] for item in delivery_data1]

                delivery_data2 = (
                    IceDelivery.objects
                    .filter(date__gte=one_week_ago)  # Filter data for the last 7 days
                    .values('date')
                    .annotate(total_ice_block_price=Sum('total_ice_block_price'))
                    .order_by('date')
                )

                labels2 = [str(item['date']) for item in delivery_data2]
                data2 = [item['total_ice_block_price'] for item in delivery_data2]
                print(labels2)
                print(data2)

                contex = {
                    'usertype': 'Admin', 'business': business,
                    'customer_length': customer_length, 'emp_length': emp_length,
                    'total_delivery': total_delivery,
                    'labels': labels, 'data': data,
                    'labels1': labels1, 'data1': data1,
                    'labels2': labels2, 'data2': data2
                }

                return render(request, 'dashboard/admin_dash_iceb.html', contex)
            elif business == "rent":
                house_length = len(House.objects.all())
                rp_length = len(RentalPerson.objects.all())
                rpayment_length = len(RentPayment.objects.all())
                emp_length = len(users.all())
                return render(request, 'dashboard/admin_dash_rent.html',
                              {'usertype': 'Admin', 'business': business,
                               'house_length': house_length, 'rpayment_length': rpayment_length, 'rp_length': rp_length,
                               'emp_length': emp_length
                               })
            elif business == "rowater":
                emp_length = len(users.all())
                customer_length = len(RowaterCustomer.objects.all())
                delivery_length = len(RowaterDelivery.objects.all())
                # delivery_data = (
                #     RowaterCustomer.objects
                #     .filter(date__gte=date.today() - timedelta(days=7)) # Filter data for the last 7 days
                #     .values('date')
                #     .annotate(total_deliveries=Count('id'))
                #     .order_by('date')
                # )
                # labels = [str(item['date']) for item in delivery_data]
                # data = [item['total_deliveries'] for item in delivery_data]
                # delivery_data1 = (
                #     RowaterDelivery.objects
                #     .filter(date__gte=date.today() - timedelta(days=7))  # Filter data for the last 7 days
                #     .values('date')
                #     .annotate(total_ice_blocks=Sum('daily_ice_block_given'))
                #     .order_by('date')
                # )
                # labels1 = [str(item['date']) for item in delivery_data1]
                # data1 = [item['total_ice_blocks'] for item in delivery_data1]
                return render(request, 'dashboard/admin_dash_rowater.html',
                              {
                                  'usertype': 'Admin',
                                  'business': business,
                                  'customer_length': customer_length,
                                  'delivery_length': delivery_length,
                                  'emp_length': emp_length,
                                  # 'labels': labels,
                                  # 'data': data,
                                  # 'labels1': labels1,
                                  # 'data1': data1
                              })
            elif business == "icechip":
                emp_length = len(users.all())
                customer_length = len(IceChipCustomer.objects.all())
                delivery_length = len(IceChipDelivery.objects.all())
                one_week_ago = date.today() - timedelta(days=7)
                delivery_data = (
                    IceChipDelivery.objects
                    .filter(date__gte=one_week_ago)
                    .values('date')
                    .annotate(total_deliveries=Count('id'))
                    .order_by('date')
                )
                labels = [str(item['date']) for item in delivery_data]
                data = [item['total_deliveries'] for item in delivery_data]
                delivery_data1 = (
                    IceChipDelivery.objects
                    .filter(date__gte=one_week_ago)  # Filter data for the last 7 days
                    .values('date')
                    .annotate(total_ice_blocks=Sum('daily_ice_block_given'))
                    .order_by('date')
                )
                labels1 = [str(item['date']) for item in delivery_data1]
                data1 = [item['total_ice_blocks'] for item in delivery_data1]
                return render(request, 'dashboard/admin_dash_icechip.html',
                              {'usertype': 'Admin', 'business': business,
                               'customer_length': customer_length, 'delivery_length': delivery_length,
                               'emp_length': emp_length,
                               'labels': labels,
                               'data': data,
                               'labels1': labels1,
                               'data1': data1
                               })
            else:
                return render(request, 'dashboard/admin_dash.html',
                              {'usertype': 'Admin', 'business': business, 'users': users})
        else:
            business = NormalUser.objects.get(user=request.user).business.name.lower()

            if business == "farming":
                return render(request, 'dashboard/normal_dash_farm.html',
                              {'message': 'You are not an admin', 'bussiness': business})
            elif business == "milk":
                return render(request, 'dashboard/normal_dash_milk.html',
                              {'message': 'You are not an admin', 'bussiness': business})
            elif business == "transport":
                return render(request, 'dashboard/normal_dash_transport.html',
                              {'message': 'You are not an admin', 'bussiness': business})
            elif business == "iceblock":
                return render(request, 'dashboard/normal_dash_iceb.html',
                              {'message': 'You are not an admin', 'bussiness': business})
            elif business == "rent":
                return render(request, 'dashboard/normal_dash_rent.html',
                              {'message': 'You are not an admin', 'bussiness': business})
            elif business == "rowater":
                return render(request, 'dashboard/normal_dash_rowater.html',
                              {'message': 'You are not an admin', 'bussiness': business})
            elif business == "icechip":
                return render(request, 'dashboard/normal_dash_icechip.html',
                              {'message': 'You are not an admin', 'bussiness': business})
            else:
                return render(request, 'dashboard/normal_dash.html',
                              {'message': 'You are not an admin', 'bussiness': business})
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
            return redirect(dashboard)
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
