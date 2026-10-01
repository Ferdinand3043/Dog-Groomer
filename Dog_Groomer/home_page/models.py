from django.db import models
from django import forms 


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content =forms.CharField(widget=forms.Textarea, required=True)