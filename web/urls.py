from django.urls import path
from .views import *
app_name = 'web'
urlpatterns = [
    path('',index_view),
    path('contact',contact_view,name='contact'),
    # path('chat',chat_view,name='chat'),
]