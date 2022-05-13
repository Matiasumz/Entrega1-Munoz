from django import forms
from ckeditor.fields import RichTextFormField

class CerrajeroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    desempleado = forms.BooleanField(required=False)
    tarjeta_presentacion = RichTextFormField(required=False)
    
class CerrajeroBusqueda(forms.Form):
       nombre = forms.CharField(max_length=20)
       
class FutbolistaBusqueda(forms.Form):
       nombre = forms.CharField(max_length=20)  

class ProfesorBusqueda(forms.Form):
       nombre = forms.CharField(max_length=20) 


class FutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    club = forms.CharField(max_length=30)
    tarjeta_presentacion = RichTextFormField(required=False)
    ficha_club = forms.ImageField(required=False)
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    curso = forms.CharField(max_length=20)
    tarjeta_presentacion = RichTextFormField(required=False)