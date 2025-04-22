from django.db import models


class PlacesModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
