from django.db import models
from django.urls import reverse

# Create your models here.

ALBUMTYPES = (
    ('V', 'Vinyl'),
    ('C', 'CD'),
    ('D', 'Digital'),
    ('T', 'Tape')
)

class Band(models.Model):
    name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    favealbum = models.CharField('Favourite Album', max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})
    
class AlbumType(models.Model):
    date_acquired = models.DateField('date acquired')
    albumtype = models.CharField(
        max_length=1,
        choices=ALBUMTYPES,
        default=ALBUMTYPES[0][0]
    )

    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"You own this album on {self.get_albumtype_display()}"
