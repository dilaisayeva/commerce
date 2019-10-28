from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.http import HttpResponse
import dateutil.parser
from django.urls import reverse



class product_list(ListView):
    model = Product
    template_name = 'products.html'
# Create your views here.

    def get_context_data(self, *args, **kwargs):
        request=self.request
        context = super(product_list, self).get_context_data(*args, **kwargs)
        context['query']=request.GET.get('q')
        print( context['query'])
        return context 

    def get_queryset(self,*args,**kwargs):
        request=self.request
        query=request.GET.get('q')
        if query is None:
            return Product.objects.all()
        return Product.objects.filter((Q(title__icontains=query)|Q(tag__title__icontains=query)|
        Q(name__icontains=query)))

class product_detail_view(DetailView):
    model=Product
    query_set=Product.objects.all()
    template_name = 'products_detail.html'
    
  

# def product_detail_view(request,pk=None,*args,**kwargs):
#     query_set=Product.objects.get(id=pk)
#     ins=Product.objects.get_by_id(pk)
#     print(ins)
#     context={
#         'object':query_set
#     }
#     return render(request,'products_detail.html',context)


class ProductFeaturedList(ListView):
    template_name = 'product_featuredlist.html'

    def get_queryset(self):
         
        return Product.objects.featured()

    
           
class ProductFeaturedDetail(DetailView):
   
    template_name = 'product_featureddetail.html'

     
    def get_object(self,*args,**kwargs):
        id=self.kwargs.get('pk')
         
        queryset=Product.objects.featured()
        qs=queryset.get_by_id(id)
        print(qs)
        if  qs is None :
            return print("Product doesn't exists")
        return qs
class ProductSlugFeaturedList(ListView):
    template_name = 'product_slugfeaturedlist.html'

    def get_queryset(self):
        return Product.objects.featured()


class ProductSlugFeaturedDetail(DetailView):
   
    template_name = 'product_slugfeatureddetail.html'

     
    def get_object(self,*args,**kwargs):
        slug=self.kwargs.get('slug')
         
        queryset=Product.objects.featured()
        qs=queryset.get_by_slug(slug)
        print(qs)
        if  qs is None :
            return print("Product doesn't exists")
        return qs


