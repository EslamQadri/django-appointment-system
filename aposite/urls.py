from django.urls import path
from . import views
from django.views import View


urlpatterns = [
    path('login', getattr(views, 'loginn'), name='login'),
    path('Registration', views.Registration,name='Registration'),
    path('logout', views.logoutt,name='logout'),

    #  User Links
    path('UserViwe', views.UserViwe, name='UserViwe'),
    path('Reserve', views.Reserve, name='Reserve'),
    path('All_Apointementsforuser', views.All_Apointementsforuser, name='All_Apointementsforuser'),
    path('Cancelforuser', views.Cancelforuser, name='Cancelforuser'),
    path('Cancel/<int:id>', views.Cancelforuserbyid, name='Cancelforuserbyid'),
    path('Reschedule',views.Reschedule,name='Reschedule'),
    path('Reschedulebyid/<int:id>', views.Reschedulebyid, name='Rescheduleby'),
    #Admin Links
    path('AdminViwe', views.AdminViwe, name='AdminViwe'),
    path('AdminApprove/<int:id>',views.AdminApprove,name='AdminApprove'),
    path('allrequests',views.allrequests,name='allrequests'),
    path('ApproveRequest', views.ApproveRequest, name='ApproveRequest'),
    path("Cancel",views.Cancel,name='Cancel'),
    path('Cancelbyid/<int:id>', views.Cancelbyid, name='Cancelbyid'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('last', views.last, name='last'),
    path('asmissed/<int:id>', views.asmissed, name='asmissed'),
    path('asfinished<int:id>', views.asfinished, name='asfinished'),
]
