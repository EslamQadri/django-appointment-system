from django.urls import path
from . import views
urlpatterns = [
    path('login', views.loginn, name='login'),
    path('Registration', views.Registration,name='Registration'),
    path('logout', views.logoutt,name='logout'),

    #  User Links
    path('UserViwe', views.UserViwe, name='UserViwe'),
    path('Reserve', views.Reserve, name='Reserve'),
    path('All_Apointementsforuser', views.All_Apointementsforuser, name='All_Apointementsforuser'),
    #Admin Link
    path('AdminViwe', views.AdminViwe, name='AdminViwe'),
    
]
