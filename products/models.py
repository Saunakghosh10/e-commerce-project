from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

class Product(models.Model):

    id = models.PositiveIntegerField(primary_key=True)
    img = models.TextField(default="URL", blank=False, null=False)
    name = models.CharField(default="Product", max_length=128, blank=False, null=False)
    desc = models.TextField(default="No Description", blank=False)
    price = models.DecimalField(default=0.0, max_digits=5, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id", "price", "-price", "name", "-name"]
