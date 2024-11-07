from django.db import models

# Create your models here.

class Persona(models.Model):
    primer_nombre=models.CharField(max_length=50)
    segundo_nombre=models.CharField(max_length=50)
    primer_apellido=models.CharField(max_length=50)
    segundo_apellido=models.CharField(max_length=50)
