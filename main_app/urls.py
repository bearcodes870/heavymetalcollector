from django.urls import path
from main_app.views import BandList
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bands/', views.bands_index, name='index'),
  path('bands/<int:band_id>/', views.bands_detail, name='detail'),
  path('bands/create', views.BandCreate.as_view(), name='bands_create'),
  path('bands/<int:pk>/update/', views.BandUpdate.as_view(), name='bands_update'),
  path('bands/<int:pk>/delete/', views.BandDelete.as_view(), name='bands_delete'),
  path('bands/<int:band_id>/add_albumtype/', views.add_albumtype, name='add_albumtype'),
  path('instruments/', views.InstrumentList.as_view(), name='instruments_index'),
  path('bands/<int:band_id>/assoc_instrument/<int:instrument_id>/', views.assoc_instrument, name='assoc_instrument'),
  path('instruments/<int:pk>/', views.InstrumentDetail.as_view(), name='instruments_detail'),
  path('instruments/create/', views.InstrumentCreate.as_view(), name='instruments_create'),
  path('instruments/<int:pk>/update/', views.InstrumentUpdate.as_view(), name='instruments_update'),
  path('instruments/<int:pk>/delete/', views.InstrumentDelete.as_view(), name='instruments_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]

