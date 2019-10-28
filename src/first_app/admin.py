from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','createdate','updatedate']


admin.site.register(Product,ProductAdmin)
