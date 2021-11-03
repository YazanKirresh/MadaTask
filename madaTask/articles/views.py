
# Create your views here.

from django.db.models.query import QuerySet
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .models import Customer
from .forms import customerRegistrationForm
from django.contrib import messages
from .filters import customerFilter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login.html")
    return render(request,"customerList.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form': form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
    else:
        form = UserCreationForm
    return render(request,"signup.html",{'form':form})


def display_customers(request):
    results = Customer.objects.all()
    myFilter = customerFilter(request.GET, queryset = results)
    results = myFilter.qs
    return render(request,"customerList.html", {"Customer":results, 'myFilter': myFilter})


def home_view(request):
    context = {}
    return render(request, "home.html", context)


def contact_view(request):
    context = {}
    return render(request, "contact.html", context)


def data_view(request):
    obj = Customer.objects.get(id = 2)
    context = {
        "object": obj
    }
    return render(request, "data.html", context)


def customer_register(request):
    context = {"form": customerRegistrationForm}
    return render(request, "register.html", context)


def add_customer(request):
    if request.method == "POST":
        form = customerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('home')


def model_form_view(request):
    context = {
        'modelform':customerRegistrationForm
    }
    return render(request, "modelform.html", context)


def edit_customer(request,pk):
    dispCustomers = Customer.objects.get(id = pk)
    return render(request,"edit.html", {"Customer":dispCustomers})


def update_customer(request,pk):
    updatecust = Customer.objects.get(id = pk)
    form = customerRegistrationForm(instance=updatecust)
    context = {'form':updatecust}
    if request.method == "POST":
        form = customerRegistrationForm(request.POST, instance=updatecust)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated..!")
            return render(request,"customerList.html", context)
    return redirect('display_customers')


def delete_customer(request,pk):
    deletecust = Customer.objects.get(id = pk)
    if request.method == "POST":
        deletecust.delete()
        return redirect('display_customers')
    context = {'item':deletecust}
    return render(request, "delete.html", context)