from django.forms import ModelForm
from .models import AlbumType

class AlbumTypeForm(ModelForm):
  class Meta:
    model = AlbumType
    fields = ['date_acquired', 'albumtype']