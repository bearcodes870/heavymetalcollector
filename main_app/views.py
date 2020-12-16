from django.shortcuts import render
from .models import Band

# Create your views here.

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello from the void</h1>')

def about(request):
  return render(request, 'about.html')

def bands_index(request):
  bands = Band.objects.all()
  return render(request, 'bands/index.html', { 'bands': bands })