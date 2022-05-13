from django.shortcuts import redirect, render


from .forms import CerrajeroBusqueda , CerrajeroFormulario,FutbolistaFormulario,ProfesorFormulario, FutbolistaBusqueda , ProfesorBusqueda
from .models import Cerrajero,Futbolista,Profesor
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def crear_cerrajero(request):
    
    if request.method == "POST":
        form = CerrajeroFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            cerrajero = Cerrajero(nombre=data["nombre"],apellido=data["apellido"],desempleado=data["desempleado"],tarjeta_presentacion=data["tarjeta_presentacion"])
            cerrajero.save()
            return redirect("index")
            
    form = CerrajeroFormulario()
    return render (request,"profesionales/crear_cerrajero.html ", {'form': form})

@login_required
def crear_futbolista(request):
    
    if request.method == "POST":
        form = FutbolistaFormulario(request.POST,request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            futbolista = Futbolista(nombre=data["nombre"],apellido=data["apellido"],club=data["club"],tarjeta_presentacion=data["tarjeta_presentacion"],ficha_club=data["ficha_club"])
            futbolista.save()
            return redirect("index")
            
    form = FutbolistaFormulario()
    return render (request,"profesionales/crear_futbolista.html ", {'form': form})

@login_required
def crear_profesor(request):
    
    if request.method == "POST":
        form = ProfesorFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            profesor = Profesor(nombre=data["nombre"],apellido=data["apellido"],curso=data["curso"],tarjeta_presentacion=data["tarjeta_presentacion"])
            profesor.save()
            return redirect("index")
            
    form = ProfesorFormulario()
    return render (request,"profesionales/crear_profesor.html ", {'form': form})


def lista_cerrajeros(request):
   
    nombre_a_buscar = request.GET.get("nombre",None)
    
    if nombre_a_buscar is not None:
        cerrajeros = Cerrajero.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        cerrajeros = Cerrajero.objects.all() 
   #
  
    form = CerrajeroBusqueda()
    return render(request,"profesionales/lista_cerrajeros.html",{"form":form,"cerrajeros":cerrajeros})


def lista_futbolistas(request):
   
    nombre_a_buscar = request.GET.get("nombre",None)
    
    if nombre_a_buscar is not None:
        futbolistas = Futbolista.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        futbolistas = Futbolista.objects.all() 
   #
  
    form = FutbolistaBusqueda()
    return render(request,"profesionales/lista_futbolistas.html",{"form":form,"futbolistas":futbolistas})


def lista_profesores(request):
   
    nombre_a_buscar = request.GET.get("nombre",None)
    
    if nombre_a_buscar is not None:
        profesores = Profesor.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        profesores = Profesor.objects.all() 
   #
  
    form = ProfesorBusqueda()
    return render(request,"profesionales/lista_profesores.html",{"form":form,"profesores":profesores})



#Creo las clases basadas en vista con detalle,editar y borrar 

class DetalleCerrajero(DetailView):
    model = Cerrajero
    template_name = "profesionales/detalle_cerrajero.html"
    
class EditarCerrajero(LoginRequiredMixin,UpdateView):
    model = Cerrajero
    success_url ="/profesionales/cerrajeros"
    fields =["nombre","apellido","desempleado"]
    

class BorrarCerrajero(LoginRequiredMixin,DeleteView):
    model = Cerrajero
    success_url = "/profesionales/cerrajeros/"


class DetalleFutbolista(DetailView):
    model = Futbolista
    template_name = "profesionales/detalle_futbolista.html"
    
class EditarFutbolista(LoginRequiredMixin,UpdateView):
    model = Futbolista
    success_url = "/profesionales/futbolistas/"
    fields=["nombre","apellido","club"]

class BorrarFutbolista(LoginRequiredMixin,DeleteView):
    model = Futbolista
    success_url = "/profesionales/futbolistas/"


class DetalleProfesor(DetailView):
    model = Profesor
    template_name = "profesionales/detalle_profesor.html"
    
class EditarProfesor(LoginRequiredMixin,UpdateView):
    model = Profesor
    success_url = "/profesionales/profesores/"
    fields=["nombre","apellido","curso"]

class BorrarProfesor(LoginRequiredMixin,DeleteView):
    model = Profesor
    success_url = "/profesionales/profesores/"