
import django_filters
from .models import *
from django_filters import CharFilter



class customerFilter(django_filters.FilterSet):
    #fname = CharFilter(field_name='customerFirstName',lookup_expr='icontains')
    #lname = CharFilter(field_name='customerLastName',lookup_expr='icontains')
    #slevel = CharFilter(field_name='customerServiceLevel',lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = '__all__' 
        #exclude =('')

    