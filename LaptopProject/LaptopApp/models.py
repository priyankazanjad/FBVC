from django.db import models

class Laptop(models.Model):
    company = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    ram = models.IntegerField()
    rom = models.FloatField()
    processor = models.CharField(max_length=30)
    price = models.FloatField()
    weight = models.FloatField()

# Create your models here.
