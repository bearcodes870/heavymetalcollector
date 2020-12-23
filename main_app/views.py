from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Band, Instrument
from .forms import AlbumTypeForm


# Create your views here.

from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bands_index(request):
  bands = Band.objects.all()
  return render(request, 'bands/index.html', { 'bands': bands })

def bands_detail(request, band_id):
  band = Band.objects.get(id=band_id)
  albumtype_form = AlbumTypeForm()
  return render(request, 'bands/detail.html', { 
    'band': band,
    'albumtype_form': albumtype_form
  })

def add_albumtype(request, band_id):
  form = AlbumTypeForm(request.POST)
  if form.is_valid():
    new_albumtype = form.save(commit=False)
    new_albumtype.band_id = band_id
    new_albumtype.save()
  return redirect('detail', band_id=band_id)

class BandList(ListView):
  model = Band
  template_name = 'bands/index.html'

class BandCreate(CreateView):
  model = Band
  fields = '__all__'
  success_url = '/bands/'

class BandUpdate(UpdateView):
  model = Band
  fields = ['favealbum']

class BandDelete(DeleteView):
  model = Band
  success_url = '/bands/'

class InstrumentList(ListView):
  model = Instrument

class InstrumentDetail(DetailView):
  model = Instrument

class InstrumentCreate(CreateView):
  model = Instrument
  fields = '__all__'

class InstrumentUpdate(UpdateView):
  model = Instrument
  fields = ['name', 'style']

class InstrumentDelete(DeleteView):
  model = Instrument
  success_url = '/instruments/'