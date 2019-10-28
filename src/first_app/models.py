from django.db import models
from django.http import Http404
from django.urls import reverse_lazy,reverse
from django.db.models import Q
 
class Contact(models.Model):
    name=models.CharField("Ad", max_length=20)
    title=models.CharField("Basliq", max_length=20)
    text=models.TextField("Movzu" )
    email=models.EmailField("Email",max_length=20)


    def __str__(self):
        return f'{self.name} {self.title}'
         
class ProductQuerySet(models.query.QuerySet):

    def featured(self):
        return self.filter(featured=True)
    def get_by_id(self,id):
        return self.get(id=id)    
    def get_by_slug(self,slug):
        return self.get(slug=slug)       
    def search(self,query):
        looksup=(Q(title__icontains=query)|Q(tag_set__title__icontains=query)|
        Q(name__icontains=query))
        return self.filter(looksup).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self,id):
        qs=self.get_queryset().get(id=id)
        if qs is None:
            raise Http404("Poll does not exist")
        return qs 
    def get_by_slug(self,slug):
        return self.get_queryset().get(slug=slug)     

    def search(self,query):
        return self.get_queryset().search(query)
    # def get_featured(self):
    #     return Product.objects.filter(featured=True)    

class Product(models.Model):
    name=models.CharField(max_length=20)
    title=models.TextField()
    slug=models.SlugField(default='abc')
    price=models.DecimalField(decimal_places=2,max_digits=5)
    image=models.FileField(upload_to='products/',null=True,blank=True)
    featured=models.BooleanField(default=False)
    createdate=models.DateTimeField(auto_now=True)
    updatedate=models.CharField(max_length=50,default='ghbj')
   
    def __str__(self):
        return self.name

        
    def get_absolute_url(self):
        return reverse('first:detail', kwargs={'pk': self.id})

        # return (f'/detail/{self.id}') 

