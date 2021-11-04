
# Create your views here.

from django.db.models.query import QuerySet
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .models import Customer, Service
from .forms import customer_registration_form, signup_form
from django.contrib import messages
from .filters import customerFilter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users,admin_only


@allowed_users(allowed_roles=['admin','customer'])
def profile_page(request):
    return render(request,"profile.html")
    

def display_services(request):
    results = Service.objects.all()
    #my_filter = customerFilter(request.GET, queryset = results)
    #results = my_filter.qs
    return render(request,"servicelist.html",{"Service":results})#, {"Service":results, 'my_filter': my_filter})


def logout_view(request):
    logout(request)
    return redirect("login_view")


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST: # redirect to the page that sent the user to the login page
                return redirect(request.POST.get('next')) 
            else:
                return redirect("display_servicess")
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form': form})


@unauthenticated_user
def signup_view(request):
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            login(request,user)
            return redirect("display_servicess")
    else:
        form = signup_form
    return render(request,"signup.html",{'form':form})


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin'])
def display_customers(request):
    results = Customer.objects.all().order_by('id')
    my_filter = customerFilter(request.GET, queryset = results)
    results = my_filter.qs
    return render(request,"customerlist.html", {"Customer":results, 'my_filter': my_filter})


@login_required(login_url="/login/")
@admin_only
def home_view(request):
    context = {}
    return render(request, "home.html", context)

""" 
    <!-- <li><a href = "{% url 'list'%}"> list </a></li> -->
@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin'])
def list_view(request):
    customer = Customer.objects.all().order_by('-id')
    #service = Service.objects.all()
    context = {'customer': customer}
    return render(request, "list.html", context) """


def customer_register(request):
    context = {"form": customer_registration_form}
    return render(request, "register.html", context)


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin'])
def add_customer(request):
    if request.method == "POST":
        form = customer_registration_form(request.POST)
        if form.is_valid():
            form.save()
    return redirect('display_customers')


def model_form_view(request):
    context = {
        'modelform':customer_registration_form
    }
    return render(request, "modelform.html", context)


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin'])
def edit_customer(request,pk):
    disp_customers = Customer.objects.get(id = pk)
    return render(request,"edit.html", {"Customer":disp_customers})


@login_required(login_url="/login/")
def update_customer(request,pk):
    update_cust = Customer.objects.get(id = pk)
    form = customer_registration_form(instance=update_cust)
    context = {'form':update_cust}
    if request.method == "POST":
        form = customer_registration_form(request.POST, instance=update_cust)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated..!")
            return render(request,"customerlist.html", context)
    return redirect('display_customers')


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['admin'])
def delete_customer(request,pk):
    delete_cust = Customer.objects.get(id = pk)
    if request.method == "POST":
        delete_cust.delete()
        return redirect('display_customers')
    context = {'item':delete_cust}
    return render(request, "delete.html", context)