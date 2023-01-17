from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    unitPrice = models.DecimalField(max_digits=5, decimal_places=2)
    quantityPerUnit = models.IntegerField()
    unitWeight = models.DecimalField()
    discount = models.DecimalField()
    color = models.CharField(max_length=50)
    image = models.CharField(max_length=150)
