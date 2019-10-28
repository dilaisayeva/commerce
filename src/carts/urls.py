from django.urls import path
from .views import *
app_name='cart'

urlpatterns=[
    path('home/',cart_home,name='home')
]