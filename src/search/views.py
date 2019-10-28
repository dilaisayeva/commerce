from django.shortcuts import render
from first_app.models import *
from django.views.generic.list import ListView


class search_product_list(ListView):
    model = Product
    # query_set = Product.objects.all()
    template_name = 'search.html'


    def get_queryset(self,*args,**kwargs):
        request=self.request
        q=request.GET.get('q')
        return Product.objects.filter(name__icontains=q)

    