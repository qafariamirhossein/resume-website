from django.contrib import admin
from .models import *

admin.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject','email')



