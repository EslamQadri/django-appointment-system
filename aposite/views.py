import re
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import  require_http_methods
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import loginForm,dform
from . models import appointments
# Create your views here.

def loginn(request):
   
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['email']
        password1 = request.POST['password']
        us=authenticate(username=username, password=password1)
      
        if us is not None:
            login(request,us) 
           
            if us.is_staff:
                return redirect('AdminViwe')
            else :
                return redirect('UserViwe')
           
        else :
            messages.error(request,'You need to login')
            return render(request, 'login/login.html',{'FF':loginForm}) 
    return render(request, 'login/login.html',{'FF':loginForm})
def Registration(request):
    pass
def logoutt(request):
    logout(request)
    messages.success(request,'you are logged out')
    return render(request, 'login/logout.html')

@login_required(login_url='login')
def UserViwe(request):
    user = request.user
    return render(request, 'user_view/user.html',{'user':user})

@login_required(login_url='login')    
def Reserve(request):
    user = request.user
    if request.method=='POST':
        date= request.POST['Reserve']
        form =dform(request.POST)
        if form.is_valid():
            form.instance.user=user
            form.save()
            messages.success(request,'Your Request in send to admin to approve it ')

            return redirect('Reserve')

        else :
            messages.error(request,'You Have Error ')
            return redirect('Reserve')

       

        
    return render(request, 'user_view/Reserve.html',{'user':user,'dform':dform})

@login_required(login_url='login')    
def All_Apointementsforuser (request):
    user= request.user
    query=appointments.objects.filter(user=user)
    return render(request, 'user_view/AllApointements.html',{'details':query})

@login_required(login_url='login')    
def Cancelforuser(request):
    user= request.user
    query=appointments.objects.filter(user=user)
    return render(request, 'user_view/Cancelforuser.html',{'details':query})
@login_required(login_url='login')    
def Cancelforuserbyid(request,id):
    user= request.user
    appointments.objects.filter(user=user).filter(id=id).delete()
    return redirect('Cancelforuser')

@login_required(login_url='login')    
def Reschedule(request):
    user= request.user
    query=appointments.objects.filter(user=user)
    return render(request, 'user_view/Reschedule.html',{'details':query})

@login_required(login_url='login')    
@require_http_methods(['POST'])
def Reschedulebyid(request,id):    
    
    print(request.POST)
    if request.method == 'POST':
        date =request.POST['date']
        user= request.user
        appointments.objects.filter(user=user,id=id).update(Reserve=date,approve=False) 
        return redirect('Reschedule')
    
    return redirect('Reschedule')
@login_required(login_url='login')    
def AdminViwe(request):
    user= request.user

    return render(request, 'admin_view/AdminHome.html',{'user':user,})

@login_required(login_url='login')    
@require_http_methods(['POST'])
def AdminApprove(request,id):
    if request.POST:
        user=request.POST.get('user')
        appointments.objects.filter(user__username=user,id=id).update(approve=True) 
        return redirect("allrequests")

    return redirect("allrequests")

@login_required(login_url='login')    
def allrequests(request):
    user= request.user
    query=appointments.objects.all()
    return render(request, 'admin_view/all.html',{'user':user,'query':query})

@login_required(login_url='login')    
def ApproveRequest(request):
    user= request.user
    query=appointments.objects.filter(approve=True)
    return render(request, 'admin_view/all.html',{'user':user,'query':query})