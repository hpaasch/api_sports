from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    position = models.CharField(max_length=5)
    birth_year = models.IntegerField()
