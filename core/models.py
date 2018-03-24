
from django.db import models


class Product(models.Model):
    SIZE_CHOICES = (
        (1, 'small'),
        (2, 'medium'),
        (3, 'large')
    )

    name = models.CharField(max_length=100)
    in_stock = models.BooleanField()
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    size = models.PositiveSmallIntegerField(choices=SIZE_CHOICES, null=True, blank=True)
