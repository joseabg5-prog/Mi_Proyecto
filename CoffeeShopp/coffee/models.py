from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantify = models.IntegerField()
    image = models.CharField(max_length=2083)
