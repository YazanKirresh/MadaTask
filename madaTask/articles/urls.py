from django.urls import path, include
#from django.conf.urls import url
from . import views


urlpatterns = [

    path('', views.home_view,name= 'home'), # index
    path('contact/', views.contact_view,name= 'contact_view'),
    path('data/', views.data_view,name= 'data_view'),
    path('register/', views.customer_register,name = 'customer_register'),
    path('addcustomer/', views.add_customer,name = 'add_customer'),
    path('modelform/', views.model_form_view,name = 'model_form_view'),
    path('customerslist/', views.display_customers,name = 'display_customers'),
    path('edit/<int:pk>', views.edit_customer,name = 'edit_customer'),
    path('updatecustomer/<int:pk>', views.update_customer,name = 'update_customer'),
    path('deletecustomer/<int:pk>', views.delete_customer,name = 'delete_customer'),
    #url(r'^signup/$', views.signupView,name = 'signup'),
    path('signup/', views.signup_view,name = 'signup_view'),
    path('login/', views.login_view,name = 'login_view'),
    path('logout/', views.logout_view,name = 'logout_view'),
    
]
