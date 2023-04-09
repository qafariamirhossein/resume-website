from django.shortcuts import render
from .forms import *
from django.contrib import messages


def index_view(request):
    return render(request, 'index.html',)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'thanks your ticket sent successfuly')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt sent successfuly')
            
    else:
        form = ContactForm()
    return render(request,'index.html',{'form':form})