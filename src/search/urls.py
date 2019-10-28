from django.urls import path
from .views import *

app_name='search'

urlpatterns=[
    path('search/',search_product_list.as_view(),name='search')
]

