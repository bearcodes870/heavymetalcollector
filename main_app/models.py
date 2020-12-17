from django.db import models
from django.urls import reverse

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    favealbum = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})