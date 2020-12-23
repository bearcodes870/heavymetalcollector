from django.contrib import admin
from .models import Band, AlbumType, Instrument

# Register your models here.

admin.site.register(Band)
admin.site.register(AlbumType)
admin.site.register(Instrument)