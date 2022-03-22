from django.db import models
from django.db.models.fields import AutoField, CharField
from accounts.models import User
from datetime import datetime
import pytz

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.TextField(default="", blank=True)
    price = models.FloatField(default=0.00)
    address = models.CharField(default="no address",max_length=256, blank=False)
    datetime = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Kolkata')))