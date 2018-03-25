
from django.db import models


class Product(models.Model):
    SIZE_CHOICES = (
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large'),
    )

    name = models.CharField(max_length=100)
    in_stock = models.BooleanField()
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    size = models.CharField(max_length=100, choices=SIZE_CHOICES, null=True, blank=True)
