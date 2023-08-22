from django.shortcuts import render
from .forms import CustomerForm, DeliveryForm
# Create your views here.
def create_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'create_customer.html', {'form': form,'message': 'Customer created successfully.'})
            else:
                return render(request, 'create_customer.html', {'form': form,'message': 'Customer creation failed.'})
        else:
            form = CustomerForm()
        return render(request, 'create_customer.html', {'form': form})
    else:
        return render(request, 'users/not_loggedin.html', {'message': 'You need to login first.'})
