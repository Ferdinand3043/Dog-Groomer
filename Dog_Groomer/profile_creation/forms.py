from django import forms
from django.core.validators import RegexValidator
from django.db import models



class OnlineAccess(forms.Form):
    First_Name = forms.CharField(max_length= 100, required=True)
    Last_Name = forms.CharField(max_length=100, required=True)
    Email = forms.EmailField(required=True)
    Phone_Number = forms.IntegerField()
    Username = forms.CharField(max_length=100, required=True)
    Password = forms.CharField(max_length=100, required=True)
