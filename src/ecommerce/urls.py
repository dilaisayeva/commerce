"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name='home'),
    path('Login/',login_page,name='login'),
    path('register/',register_page,name='register'),
    path('',include('first_app.urls',namespace='first')),
    path('boostrap/',TemplateView.as_view(template_name=('boostrap/example.html'))),
    path('',include('search.urls',namespace='search')),
    path('cart/',include('carts.urls',namespace='cart')),
    path('contact/',contact_page.as_view(),name='contact')
]

if settings.DEBUG:
     urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
