from django.db import models


class Aerosol(models.Model):
    
    marca = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

