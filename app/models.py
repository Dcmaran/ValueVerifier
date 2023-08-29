from django.db import models


# Create your models here.

class Conversion(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    input = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    output = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    currency = models.CharField(max_length=3, null=True)
    converted_currency = models.CharField(max_length=3, null=True)
