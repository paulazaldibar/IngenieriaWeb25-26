from django.contrib import admin
from django.utils.html import format_html
from .models import Aerolinea, Pais, Aeropuerto

admin.site.register(Aerolinea)
admin.site.register(Pais)
admin.site.register(Aeropuerto)

# Personalizar el panel de administración
admin.site.site_header = "Panel de Administración – Proyecto Volare"
admin.site.site_title = "Administrador Volare"
admin.site.index_title = "Bienvenido al panel de gestión de Volare"


# Colores por cada país
PAIS_COLORES = {
    'España': '#DC143C',
    'Italia': '#4dc493',
    'Alemania': '#FF7F50',
    'Catar': "#881834",               
    'Emiratos Árabes Unidos': "#135A40",
    'Estados Unidos': "#33339F",     
    'Francia': "#879AFA",            
    'Países Bajos': "#F5D716",       
    'Reino Unido': "#9B2AB7",        
    'Suiza': "#E881B5FF",               
}

# AEROLINEAS
admin.site.unregister(Aerolinea) # quitamos el modelo que ya estaba registrado
@admin.register(Aerolinea) # registramos de nuevo con la configuración personalizada
class AerolineaAdmin(admin.ModelAdmin):
    list_display = ('nombre_color', 'siglas', 'pais_origen')
    search_fields = ('nombre', 'siglas')
    list_filter = ('pais_origen',)
    ordering = ['nombre']
    list_per_page = 10
    exclude = ('siglas',)

    def nombre_color(self, obj):
        color = PAIS_COLORES.get(obj.pais_origen.nombre, '#000000')
        return format_html(f'<span style="color:{color};">{obj.nombre}</span>')
    nombre_color.short_description = 'Nombre (color)'


# PAISES
admin.site.unregister(Pais)
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curiosidad')
    search_fields = ('nombre',)
    ordering = ['nombre']
    list_filter = ('nombre',)
    list_per_page = 10


# AEROPUERTOS
admin.site.unregister(Aeropuerto)
@admin.register(Aeropuerto)
class AeropuertoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'pais')
    search_fields = ('nombre', 'siglas')
    list_filter = ('pais',)
    ordering = ['nombre']
    list_per_page = 10


