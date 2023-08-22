from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import AdminUser, NormalUser, Business
from dashboard.views import dashboard

# Create your views here.
def login_admin(request):
    if request.user.is_authenticated:
        return redirect(dashboard)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        business_name = request.POST['business_name']
        try:
            business = Business.objects.get(name=business_name)
        except Business.DoesNotExist:
            return render(request, 'users/login_admin.html', {'error_message': 'Business does not exist'})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                admin_user = AdminUser.objects.get(user=user, business=business)
                login(request, user)
                return redirect(dashboard)
            except AdminUser.DoesNotExist:
                return render(request, 'users/login_admin.html', {'error_message': 'User is not an admin'})
        else:
            return render(request, 'users/login_admin.html', {'error_message': 'Invalid login'})
    business_list = Business.objects.all()
    return render(request, 'users/login_admin.html', {'business_list': business_list})

# view for logging in a normal user
def login_normal(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        business_name = request.POST['business_name']
        try:
            business = Business.objects.get(name=business_name)
        except Business.DoesNotExist:
            return render(request, 'users/login_normal.html', {'error_message': 'Business does not exist'})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                normal_user = NormalUser.objects.get(user=user, business=business)
                login(request, user)
                return HttpResponseRedirect("Authenticated")
            except NormalUser.DoesNotExist:
                return render(request, 'users/login_normal.html', {'error_message': 'User is not a normal user'})
        else:
            return render(request, 'users/login_normal.html', {'error_message': 'Invalid login'})
    business_list = Business.objects.all()
    return render(request, 'users/login_normal.html', {'business_list': business_list})

# view for logging out a user
@login_required
def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')


# def dashboard(request):
#     if request.user.is_authenticated:
#         final = is_admin(request.user)
#         if final:
#             form = NormalUserForm()
#             if request.method == 'POST':
#                 form = NormalUserForm(request.POST)
#                 if form.is_valid():
#                     username = form.cleaned_data['username']
#                     password = form.cleaned_data['password']
#                     business_name = form.cleaned_data['business_name']
#                     try:
#                         business = Business.objects.get(name=business_name)
#                     except Business.DoesNotExist:
#                         return render(request, 'admin_dash.html', {'message': 'Business does not exist'})
#                     user = User.objects.create_user(username=username, password=password)
#                     normal_user = NormalUser(user=user, business=business)
#                     normal_user.save()
#                     return render(request, 'admin_dash.html', {'message': 'User created successfully'})
#                 else:
#                     return render(request, 'admin_dash.html', {'message': 'Invalid form'})
#             return render(request, 'admin_dash.html', {'form': form})
#         else:
#             return render(request, 'normal_dash.html')
#     else:
#         return render(request, 'not_loggedin.html')
