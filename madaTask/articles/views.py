
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
from django.contrib.auth.decorators import login_required


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("contact.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST: # redirect to the page that sent the user to the login page
                return redirect(request.POST.get('next')) 
            else:
                return redirect("home")
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


@login_required(login_url="/login/")
def display_customers(request):
    results = Customer.objects.all()
    my_filter = customerFilter(request.GET, queryset = results)
    results = my_filter.qs
    return render(request,"customerlist.html", {"Customer":results, 'my_filter': my_filter})


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


@login_required(login_url="/login/")
def add_customer(request):
    if request.method == "POST":
        form = customerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('display_customers')


def model_form_view(request):
    context = {
        'modelform':customerRegistrationForm
    }
    return render(request, "modelform.html", context)


@login_required(login_url="/login/")
def edit_customer(request,pk):
    disp_customers = Customer.objects.get(id = pk)
    return render(request,"edit.html", {"Customer":disp_customers})


@login_required(login_url="/login/")
def update_customer(request,pk):
    update_cust = Customer.objects.get(id = pk)
    form = customerRegistrationForm(instance=update_cust)
    context = {'form':update_cust}
    if request.method == "POST":
        form = customerRegistrationForm(request.POST, instance=update_cust)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated..!")
            return render(request,"customerlist.html", context)
    return redirect('display_customers')


@login_required(login_url="/login/")
def delete_customer(request,pk):
    delete_cust = Customer.objects.get(id = pk)
    if request.method == "POST":
        delete_cust.delete()
        return redirect('display_customers')
    context = {'item':delete_cust}
    return render(request, "delete.html", context)