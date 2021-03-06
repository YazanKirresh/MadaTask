from django.urls import path, include
#from django.conf.urls import url
from . import views


urlpatterns = [

    path('', views.home_view,name= 'home'), # index
    #path('list/', views.list_view,name= 'list'),
    path('register/', views.customer_register,name = 'customer_register'),
    path('serviceregister/', views.service_register,name = 'service_register'),
    path('addcustomer/', views.add_customer,name = 'add_customer'),
    path('addservice/', views.add_new_service,name = 'add_service'),
    path('customerslist/', views.display_customers,name = 'display_customers'),
    path('servicelist/', views.display_services,name = 'display_servicess'),
    path('edit/<int:pk>', views.edit_customer,name = 'edit_customer'),
    path('updatecustomer/<int:pk>', views.update_customer,name = 'update_customer'),
    path('deletecustomer/<int:pk>', views.delete_customer,name = 'delete_customer'),
    path('signup/', views.signup_view,name = 'signup_view'),
    path('login/', views.login_view,name = 'login_view'),
    path('logout/', views.logout_view,name = 'logout'),
    path('profile/', views.profile_page,name = 'profile'),
    
]
