from django.contrib import admin
from .models import Band, AlbumType

# Register your models here.

admin.site.register(Band)
admin.site.register(AlbumType)