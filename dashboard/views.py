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
            return render(request, 'dashboard/admin_dash.html', {'usertype': 'Admin', 'business': business, 'users': users})
        else:
            return render(request, 'dashboard/admin_dash.html', {'usertype': 'Normal'})
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
        final = is_admin(request.user)
        if final:
            form = NormalUserForm()
            if request.method == 'POST':
                form = NormalUserForm(request.POST)
                if form.is_valid():
                    user= form.cleaned_data['user']
                    business = form.cleaned_data['business']
                    is_admin1 = form.cleaned_data['is_admin']
                    normal_user = NormalUser(user=user, business=business, is_admin=is_admin1)
                    normal_user.save()
                    return redirect('display_user',business_id=business.id)
                else:
                    return render(request, 'dashboard/add_normal.html', {'message': 'Invalid form'})
            return render(request, 'dashboard/add_normal.html', {'form': form})
        else:
            return render(request, 'dashboard/normal_dash.html', {'message': 'You are not an admin'})
    else:
        return render(request, 'users/not_loggedin.html')