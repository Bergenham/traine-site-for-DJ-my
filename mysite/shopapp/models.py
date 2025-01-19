from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    """ Hi
    sds: :model:`shopapp.Order`
    """
    class Meta:
        ordering = ('-prise', 'name',)

    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True, db_index=True)
    prise = models.DecimalField(max_digits=8, default=0, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    arvay = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Product (pk - {self.pk},name - {self.name!r} )'


class Order(models.Model):
    delivery_adres = models.TextField(null=False, blank=True)
    promocod = models.CharField(max_length=20, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')