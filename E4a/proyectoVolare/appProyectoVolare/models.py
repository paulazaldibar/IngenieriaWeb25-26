from django.db import models
from django.db import models

class Aerolinea(models.Model):
    id_aerolinea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='logos_aerolineas/')
    descripcion = models.TextField()
    pais_origen = models.ForeignKey('Pais', on_delete=models.CASCADE, related_name='aerolineas_origen', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    bandera = models.ImageField(upload_to='banderas_paises/')
    curiosidad = models.TextField()
    
    def __str__(self):
        return self.nombre

class Aeropuerto(models.Model):
    id_aeropuerto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=3)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_aeropuertos/')
    aerolineas = models.ManyToManyField(Aerolinea)
    
    def __str__(self):
        return self.nombre     	
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"

