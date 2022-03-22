from django.db import models
from django.contrib.postgres.fields import JSONField

class User(models.Model):
    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    cart = models.TextField(default="", blank=True)