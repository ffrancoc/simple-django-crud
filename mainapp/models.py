from datetime import datetime
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.TextField(max_length=50, null=False, blank=False)
    apellido = models.TextField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    genero = models.CharField(max_length=2, null=False, blank=False)
    telefono = models.CharField(max_length=20, null=False, blank=False, unique=True)
    correo = models.EmailField(max_length=20, unique=True, null=True, blank=True)
    creacion = models.DateTimeField(null=False, blank=False, default=datetime.now)

    def __str__(self):
        return f"Persona({self.nombre}, {self.apellido}, {self.fecha_nacimiento}, {self.genero}, {self.telefono}, {self.correo}, {self.creacion})"
    