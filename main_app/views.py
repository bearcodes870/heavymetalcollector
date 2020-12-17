from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Band

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
  return render(request, 'bands/detail.html', { 'band': band })

class BandList(ListView):
  model = Band
  template_name = 'bands/index.html'

class BandCreate(CreateView):
  model = Band
  fields = '__all__'