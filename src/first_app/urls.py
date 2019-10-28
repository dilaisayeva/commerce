from django.urls import path
from .views import *

app_name = 'first'
urlpatterns = [
    path('list/', product_list.as_view(),name='list'),
    path('detail/<int:pk>/', product_detail_view.as_view(), name='detail'),
    path('listF/', ProductFeaturedList.as_view(), name='listF'),
    path('detailF/<int:pk>/', ProductFeaturedDetail.as_view(), name='detailF'),
    path('listS/', ProductSlugFeaturedList.as_view(), name='listS'),
    path('detailS/<slug>/', ProductSlugFeaturedDetail.as_view(), name='detailS')
]
