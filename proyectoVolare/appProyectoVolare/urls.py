from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Aerolíneas
    path('aerolineas/', views.lista_aerolineas, name='lista_aerolineas'),
    path('aerolineas/<int:aerolinea_id>/', views.detalle_aerolinea, name='detalle_aerolinea'),
    # Países
    path('paises/', views.lista_paises, name='lista_paises'),
    path('paises/<int:pais_id>/', views.detalle_pais, name='detalle_pais'),
    # Aeropuertos
    path('aeropuertos/', views.lista_aeropuertos, name='lista_aeropuertos'),
    path('aeropuertos/<int:aeropuerto_id>/', views.detalle_aeropuerto, name='detalle_aeropuerto'),
]
