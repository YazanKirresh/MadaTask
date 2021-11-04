
from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_first_name = models.CharField(max_length=30)
    customer_last_name = models.CharField(max_length=30)
    customer_service = models.ManyToManyField('Service')
    class Meta:
        db_table = 'articles_customer'
    def __str__(self):
        return self.customer_last_name


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    def __str__(self):
        return self.service_name


class Employee(models.Model):
    employee_first_name = models.CharField(max_length=30)
    employee_last_name = models.CharField(max_length=30)
    employee_allowed_access = models.BooleanField(default=False)
    employee_position = models.CharField(max_length=30)
    employee_salary = models.IntegerField(default=0)
    def __str__(self):
        return self.employee_last_name


        
