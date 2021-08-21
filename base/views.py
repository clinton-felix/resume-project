from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

# Create your views here.

def home(request):

    form = CustomerForm()
    allFilledForm = Customer.objects.all()

    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')



    context = {'form':form, 'Customers': allFilledForm }
    return render(request, 'base/home.html', context)