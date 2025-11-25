from django.urls import path
from .views import ContactoView, ContactoOKView

from .views import (
    IndexView,
    AerolineaListView, AerolineaDetailView,
    PaisListView, PaisDetailView,
    AeropuertoListView, AeropuertoDetailView,
    buscar_aeropuertos
)


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
]
