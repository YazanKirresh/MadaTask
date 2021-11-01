from django.urls import path, include
#from django.conf.urls import url
from . import views


urlpatterns = [

    path('', views.homeView,name= 'home'), # index
    path('contact/', views.contact,name= 'contact'),
    path('data/', views.data,name= 'data'),
    path('register/', views.customerRegister,name = 'register'),
    path('addcustomer/', views.addCustomer,name = 'addcustomer'),
    path('modelform/', views.modelFormView,name = 'addmodelform'),
    path('customerslist/', views.displayCustomers,name = 'customerslist'),
    path('edit/<int:pk>', views.editCustomer,name = 'editCustomer'),
    path('updatecustomer/<int:pk>', views.updateCustomer,name = 'updateCustomer'),
    path('deletecustomer/<int:pk>', views.deleteCustomer,name = 'deletecustomer'),
    #url(r'^signup/$', views.signupView,name = 'signup'),
    path('signup/', views.signupView,name = 'signupForm'),
    path('login/', views.loginView,name = 'loginFrom'),
    path('logout/', views.logoutView,name = 'logoutFrom'),
    
]
