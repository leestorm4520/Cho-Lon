from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserModel(models.Model):
    fName = models.CharField(max_length = 100)
    lName = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    address = models.CharField(max_length = 100)
    phoneNumber = models.CharField(max_length=15)

class ProductModel(models.Model):
    pName = models.CharField(max_length = 255)
    pPrice = models.DecimalField(max_digits = 10, decimal_places = 2)
    pQuantity = models.DecimalField(max_digits = 3, decimal_places = 0)
    pDesc = models.TextField()
    pDateCreated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('-pDateCreated',)

