from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login


def home_page(request):
    # name=request.POST.get('name')
    # print(name)
    form = ContactForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        # form.save()
        print(form.cleaned_data)
    return render(request, 'home_page.html', context)


def login_page(request):
    form = LoginForm()

    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        print(request.user)
        if user is not None:
            print(request.user.is_authenticated)
            context['name'] = username
            login(request, user)
            print(form.cleaned_data)
            print(username)
        else:
            print("error")
        context['form'] = LoginForm()

    return render(request, "auth/login.html", context)


def register_page(request):
    form=RegisterForm(request.POST or None)
    context={

        'form':form
    }
    
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
    return render(request,'auth/register.html',context)