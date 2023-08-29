from django.contrib.auth.models import User
from django.shortcuts import render,redirect
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
                return render(request, 'dashboard/admin_dash.html', {'usertype': 'Admin', 'business': business, 'users': users})
            elif business == "milk":
                return render(request, 'dashboard/admin_dash_milk.html', {'usertype': 'Admin', 'business': business, 'users': users})
            elif business == "transport":
                return render(request, 'dashboard/admin_dash_transport.html', {'usertype': 'Admin', 'business': business, 'users': users})
            else:
                return render(request, 'dashboard/admin_dash.html', {'usertype': 'Admin', 'business': business, 'users': users})
        else:
            return render(request, 'dashboard/normal_dash.html', {'usertype': 'Normal'})
    else:
        return render(request, 'users/not_loggedin.html')


def add_user_into_system(request):
    if request.user.is_authenticated:
        final = is_admin(request.user)  # You mentioned you have this function
        if final:
            message = ""
            if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    user.refresh_from_db()
                    user.save()
                    message = "User added successfully"
                else:
                    form = RegisterForm()
                    message = "Invalid form"
                return render(request, 'dashboard/add_user.html', {'form': form})
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
            message = ""
            if request.method == 'POST':
                form = NormalUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    message = "User added successfully"
                else:
                    form = NormalUserForm()
                    message = "Invalid form"
                return render(request, 'dashboard/add_normal.html', {'form': form, 'message': message})
            else:
                form = NormalUserForm()
                return render(request, 'dashboard/add_normal.html', {'form': form})
        else:
            return render(request, 'dashboard/normal_dash.html', {'message': 'You are not an admin'})
    else:
        return render(request, 'users/not_loggedin.html')