from django.urls import path
from .views import ContactoView, ContactoOKView

from .views import (
    IndexView,
    AerolineaListView, AerolineaDetailView,
    PaisListView, PaisDetailView,
    AeropuertoListView, AeropuertoDetailView,
    buscar_aeropuertos
)
from . import views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('aerolineas/', AerolineaListView.as_view(), name='lista_aerolineas'),
    path('aerolineas/<int:aerolinea_id>/', AerolineaDetailView.as_view(), name='detalle_aerolinea'),

    path('paises/', PaisListView.as_view(), name='lista_paises'),
    path('paises/<int:pais_id>/', PaisDetailView.as_view(), name='detalle_pais'),

    path('aeropuertos/', AeropuertoListView.as_view(), name='lista_aeropuertos'),
    path('aeropuertos/<int:aeropuerto_id>/', AeropuertoDetailView.as_view(), name='detalle_aeropuerto'),

    path('buscar_aeropuertos/', buscar_aeropuertos, name='buscar_aeropuertos'),

    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('contacto/ok/', ContactoOKView.as_view(), name='contacto_ok'),
    
    path('api/aerolineas/', views.api_aerolineas, name='api_aerolineas'),
    path('api/aerolineas/<int:aerolinea_id>/', views.api_aerolinea_detalle, name='api_aerolinea_detalle'),

    path('api/paises/', views.api_paises, name='api_paises'),
    path('api/paises/<int:pais_id>/', views.api_pais_detalle, name='api_pais_detalle'),

    path('api/aeropuertos/', views.api_aeropuertos, name='api_aeropuertos'),
    path('api/aeropuertos/<int:aeropuerto_id>/', views.api_aeropuerto_detalle, name='api_aeropuerto_detalle'),
]
