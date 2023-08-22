from django.db import models

# Create your models here.

class Conversion(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    input = models.DecimalField(max_digits=10, decimal_places=2)
    output = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    converted_currency = models.CharField(max_length=3)

