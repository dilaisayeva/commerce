from django.db import models
from django.conf import settings
from first_app.models import Product

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)