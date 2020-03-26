from django.db import models


class COVIDData(models.Model):
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
