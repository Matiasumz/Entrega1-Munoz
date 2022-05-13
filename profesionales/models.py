from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    desempleado = models.BooleanField()
    tarjeta_presentacion = RichTextField(blank=True,null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    club = models.CharField(max_length=30)
    tarjeta_presentacion = RichTextField(blank=True,null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    ficha_club = models.ImageField(upload_to='ficha', blank= True, null= True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}-{self.club}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    curso = models.CharField(max_length=20)
    tarjeta_presentacion = RichTextField(blank=True,null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}-{self.curso}"
