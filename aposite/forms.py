from django import forms
from .models import appointments
from django.contrib.auth.models import User

class loginForm(forms.ModelForm):
    class Meta:
        model =User
        fields="__all__"
        
    email = forms.CharField(label='',widget=forms.TextInput(
        attrs={'name':'username','class': 'form-control form-control-lg', 'placeholder':"User Name"}))
    password = forms.CharField(label=(""),widget=forms.PasswordInput(
         attrs={'class': 'form-control form-control-lg', 'placeholder':"Password"}
    ))
class Registrationform(forms.ModelForm):
    class Meta:
        model =User
        fields =['name', 'email', 'password']
    email = forms.EmailField(label='',widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder':"Email Address"}))
    name=forms.CharField(label="",widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder':"Your Name"}
        ))
    password1 = forms.CharField(label=(""),widget=forms.PasswordInput(
         attrs={'class': 'form-control form-control-lg ', 'placeholder':"Password"}
    ))
    password2 = forms.CharField(label=(""),widget=forms.PasswordInput(
         attrs={'class': 'form-control form-control-lg', 'placeholder':"Repet Your Password"}
    ))

class dform(forms.ModelForm):
    class Meta:
        model =appointments
        fields =['Reserve']
    Reserve= forms.DateField(label=(""),widget=forms.DateInput(
        attrs={'class': 'form-Date form-Date-lg','type':'Date'}
    #type="Date" class="Date" data-date-format="mm/dd/yyyy"
    ))
