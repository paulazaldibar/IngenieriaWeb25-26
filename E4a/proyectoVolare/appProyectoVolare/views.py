from django.shortcuts import render, get_object_or_404
from .models import Aerolinea, Pais, Aeropuerto

# ---- PORTADA ----
'''
def index(request): # una aerolínea de cada país
    paises = Pais.objects.all()
    aerolineas_por_pais = []
    for pais in paises:
        aeropuertos = pais.aeropuerto_set.all()
        aerolineas = Aerolinea.objects.filter(aeropuerto__in=aeropuertos).distinct()
        aerolineas_por_pais.append({
            'pais': pais,
            'aerolineas': aerolineas
    })

    return render(request, 'index.html', {'paises_con_aerolineas': aerolineas_por_pais})
'''

# ---- INDEX / PORTADA ----
def index(request):
    paises = Pais.objects.all()
    aerolineas_por_pais = []

    for pais in paises:
        # Obtenemos la primera aerolínea registrada de ese país
        aerolinea = Aerolinea.objects.filter(pais_origen=pais).first()
        if aerolinea:
            aerolineas_por_pais.append({
                'aerolinea': aerolinea,
                'pais': pais
            })

    return render(request, 'index.html', {'aerolineas_por_pais': aerolineas_por_pais})


# ---- AEROLÍNEAS ----
def lista_aerolineas(request):
    aerolineas = Aerolinea.objects.all()
    return render(request, 'aerolineas.html', {'aerolineas': aerolineas})

def detalle_aerolinea(request, aerolinea_id):
    aerolinea = get_object_or_404(Aerolinea, pk=aerolinea_id)
    return render(request, 'detalle_aerolinea.html', {'aerolinea': aerolinea})

# ---- PAISES ----
def lista_paises(request):
    paises = Pais.objects.all()
    return render(request, 'pais.html', {'paises': paises})

def detalle_pais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    aeropuertos = pais.aeropuerto_set.all()
    aerolineas_operando = Aerolinea.objects.filter(aeropuerto__in=aeropuertos).distinct()
    return render(request, 'detalle_pais.html', {'pais': pais, 'aeropuertos': aeropuertos, 'aerolineas_operando': aerolineas_operando,})

# ---- AEROPUERTOS ----
def lista_aeropuertos(request):
    aeropuertos = Aeropuerto.objects.all()
    return render(request, 'aeropuertos.html', {'aeropuertos': aeropuertos})

def detalle_aeropuerto(request, aeropuerto_id):
    aeropuerto = get_object_or_404(Aeropuerto, pk=aeropuerto_id)
    return render(request, 'detalle_aeropuerto.html', {'aeropuerto': aeropuerto})
