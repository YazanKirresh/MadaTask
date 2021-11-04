from django.contrib import admin
from .models import Customer,Service,Employee,Combination

# Register your models here.
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Employee)
admin.site.register(Combination)
