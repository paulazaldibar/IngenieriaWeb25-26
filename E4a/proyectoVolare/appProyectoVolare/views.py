from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactoForm
from django.views.generic import TemplateView

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
    template_name = 'aerolineas.html'
    context_object_name = 'aerolineas'

    def get_queryset(self):
        return get_list_or_404(Aerolinea)


class AerolineaDetailView(DetailView):
    model = Aerolinea
    template_name = 'detalle_aerolinea.html'
    pk_url_kwarg = 'aerolinea_id'
    context_object_name = 'aerolinea'


# -----------------------------
# PAÍSES
# -----------------------------
class PaisListView(ListView):
    template_name = 'pais.html'
    context_object_name = 'paises'

    def get_queryset(self):
        return get_list_or_404(Pais)

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
    template_name = 'aeropuertos.html'
    context_object_name = 'aeropuertos'

    def get_queryset(self):
        return get_list_or_404(Aeropuerto)


class AeropuertoDetailView(DetailView):
    model = Aeropuerto
    template_name = 'detalle_aeropuerto.html'
    pk_url_kwarg = 'aeropuerto_id'
    context_object_name = 'aeropuerto'


# -----------------------------
# FORMULARIO
# -----------------------------
class ContactoView(FormView):
    template_name = 'contact.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto_ok')

    def form_valid(self, form):
        form.save()     # Guarda el mensaje en la BD
        return super().form_valid(form)
    

class ContactoOKView(TemplateView):
    template_name = 'contact_ok.html'