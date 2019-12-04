from django.db import models
from datetime import datetime, date
# Create your models here.
class treatmen(models.Model):
   # Id = models.IntegerField(default=1)
    date = models.DateField(null=True)
    doctor=models.CharField(max_length=20)
    treatments= models.CharField(max_length=20)
    price= models.IntegerField()
    appointment = models.BooleanField(default=False)