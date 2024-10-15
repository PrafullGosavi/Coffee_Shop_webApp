from django.db import models

# Create your models here.
class Coffee(models.Model):
    name=models.CharField(max_length=255)
    price = models.FloatField()
    quantiy = models.IntegerField()
    img = models.CharField(max_length=2083)

