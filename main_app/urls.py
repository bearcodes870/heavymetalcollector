from django.urls import path
from main_app.views import BandList
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bands/', views.bands_index, name='index'),
  path('bands/<int:band_id>/', views.bands_detail, name='detail'),
  path('bands/', BandList.as_view(), name="bands_index"),
]

