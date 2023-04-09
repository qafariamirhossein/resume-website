from django import forms
from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'message', 'email']