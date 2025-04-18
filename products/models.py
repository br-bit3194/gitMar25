from django.db import models
from django.utils.timezone import datetime

class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Products(AuditModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.name

class Category(AuditModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Orders(AuditModel):
    product = models.ManyToManyField(Products, related_name='orders')
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order for {self.product.name}"