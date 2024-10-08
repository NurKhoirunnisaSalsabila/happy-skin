from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    # max_digits=3 and decimal_places=2 allows for ratings like 4.75, 5.00, etc.
    