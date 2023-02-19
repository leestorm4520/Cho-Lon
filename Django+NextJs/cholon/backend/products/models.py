from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=150)

class Product(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True, blank=True)
    unitPrice = models.DecimalField(max_digits=5, decimal_places=2)
    quantityPerUnit = models.IntegerField()
    unitWeight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    color = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=150, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True) # seller

    class Meta:
        permissions = [
            ("create_product", "Can create new product"),
            ("edit_product", "Can edit the product information")
        ]

    def __str__(self):
        return self.name + " | " + str(self.unitPrice)

class Review(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    rating =  models.IntegerField(null=True,blank=True,default=0)
    comment = models.TextField(null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id =  models.AutoField(primary_key=True,editable=False)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) # customer

    def __str__(self):
        return str(self.rating)

class OrderStatus(models.TextChoices):
    Pending = 'Pending'
    Shipped = 'Shipped'
    Delivered = 'Delivered'
    Canceled = 'Canceled'
    Delayed = 'Delayed'

class Order(models.Model):
    taxPrice = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    shippingPrice = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    totalPrice = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False,null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False,null=True, blank=True)
    status = models.CharField(
        max_length = 10,
        choices = OrderStatus.choices,
        default = OrderStatus.Pending
    )
    createdAt = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    _id =  models.AutoField(primary_key=True,editable=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True) # customer

    class Meta:
        permissions = [
            ("read_order", "Can read order's information"),
            ("edit_order", "Can create and edit order's information")
        ]
        # user.has_perm("read_order")
    def __str__(self):
        return str(self.createdAt)

class OrderDetails(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True,default=0)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    totalPrice = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    discount = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    image = models.CharField(max_length=200,null=True,blank=True)
    _id =  models.AutoField(primary_key=True,editable=False)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order  = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.name)
