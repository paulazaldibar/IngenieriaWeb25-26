from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Aerolinea, Pais, Aeropuerto

# -----------------------------
# AJAX – BUSCAR AEROPUERTOS
# -----------------------------
@csrf_exempt
def buscar_aeropuertos(request):
    texto = request.GET.get("q", "")
    aeropuertos = Aeropuerto.objects.filter(nombre__icontains=texto)
    html = render_to_string("aeropuertos_items.html", {"aeropuertos": aeropuertos})
    return JsonResponse({"html": html})


# -----------------------------
# PORTADA (INDEX)
# -----------------------------
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paises = Pais.objects.all()
        aerolineas_por_pais = []

        for pais in paises:
            aerolinea = Aerolinea.objects.filter(pais_origen=pais).first()
            if aerolinea:
                aerolineas_por_pais.append({
                    'pais': pais,
                    'aerolinea': aerolinea
                })

        context['aerolineas_por_pais'] = aerolineas_por_pais
        return context


# -----------------------------
# AEROLÍNEAS
# -----------------------------
class AerolineaListView(ListView):
    model = Aerolinea
    template_name = 'aerolineas.html'
    context_object_name = 'aerolineas'

class AerolineaDetailView(DetailView):
    model = Aerolinea
    template_name = 'detalle_aerolinea.html'
    pk_url_kwarg = 'aerolinea_id'
    context_object_name = 'aerolinea'


# -----------------------------
# PAÍSES
# -----------------------------
class PaisListView(ListView):
    model = Pais
    template_name = 'pais.html'
    context_object_name = 'paises'

class PaisDetailView(DetailView):
    model = Pais
    template_name = 'detalle_pais.html'
    pk_url_kwarg = 'pais_id'
    context_object_name = 'pais'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pais = self.get_object()

        aeropuertos = pais.aeropuerto_set.all()
        aerolineas_operando = Aerolinea.objects.filter(
            aeropuerto__in=aeropuertos
        ).distinct()

        context['aeropuertos'] = aeropuertos
        context['aerolineas_operando'] = aerolineas_operando
        return context


# -----------------------------
# AEROPUERTOS
# -----------------------------
class AeropuertoListView(ListView):
    model = Aeropuerto
    template_name = 'aeropuertos.html'
    context_object_name = 'aeropuertos'

class AeropuertoDetailView(DetailView):
    model = Aeropuerto
    template_name = 'detalle_aeropuerto.html'
    pk_url_kwarg = 'aeropuerto_id'
    context_object_name = 'aeropuerto'
