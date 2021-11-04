from django.http import HttpResponse
from django.shortcuts import redirect


# if we type @un_authenticated_user before a function
# this gets executed before the function  
# comes in here then the function


# Dont use this in real project! 
# Not best practice change before submitting
def admin_only(views_function):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect("home")

        if group == 'admin':
            return redirect("display_customers")    
    return wrapper_function

def unauthenticated_user(views_function):
    def wrapper_function(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect("contact_view")
            else:
                return views_function(request, *args, **kwargs)
    return wrapper_function


def allowed_users(allowed_roles=[]):
    def decorator(views_function):
        def wrapper_function(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return views_function(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page!")

        return wrapper_function
    return decorator
