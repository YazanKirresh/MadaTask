
from django.db import models

# Create your models here.

class Customer(models.Model):
    customerFirstName = models.CharField(max_length=30)
    customerLastName = models.CharField(max_length=30)
    customerServiceLevel = models.IntegerField(default=0)
    class Meta:
        db_table = 'articles_customer'


    def __str__(self):
        return self.customerLastName

class Service(models.Model):
    serviceName = models.CharField(max_length=50)
    serviceLevel = models.ManyToManyField('Customer', related_name = 'Services')



    def __str__(self):
        return self.serviceName

class Employees(models.Model):
    employeeFirstName = models.CharField(max_length=30)
    employeeLastName = models.CharField(max_length=30)
    employeeAllowedAccess = models.BooleanField(default=False)
    employeePosition = models.CharField(max_length=30)
    employeeSalary = models.IntegerField(default=0)
    def __str__(self):
        return self.employeeLastName


        
