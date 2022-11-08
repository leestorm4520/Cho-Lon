from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length=15)