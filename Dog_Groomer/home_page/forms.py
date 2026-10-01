from django import forms
from django.core.validators import RegexValidator
from django.db import models


class ContactForm(forms.Form):
    Name = forms.CharField(max_length=100, required=True)
    Email = forms.EmailField(required=True)
    Message = forms.CharField(widget=forms.Textarea, required=True)

