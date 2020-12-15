from django.shortcuts import render

class Band:
    def __init__(self, name, genre, firstalbum):
        self.name = name,
        self.genre = genre,
        self.favealbum = favealbum

bands = [
    Band('Megadeth', 'Speed Metal', 'Rust In Peace'),
    Band('Metallica', 'Thrash Metal', 'Ride the Lightning'),
    Band('Pallbearer', 'Sludge Metal', 'Foundations of Burden')
]

# Create your views here.

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello from the void</h1>')

def about(request):
  return render(request, 'about.html')

def bands(request):
  return render(request, 'bands/index.html', { 'bands': bands })