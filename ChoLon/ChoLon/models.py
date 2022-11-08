from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    phone_number = models.DecimalField(max_digits = 10, decimal_places = 0)