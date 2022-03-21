from django.shortcuts import redirect, render


from .forms import CerrajeroBusqueda, CerrajeroFormulario,FutbolistaFormulario,ProfesorFormulario
from .models import Cerrajero,Futbolista,Profesor

def crear_cerrajero(request):
    
    if request.method == "POST":
        form = CerrajeroFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            cerrajero = Cerrajero(nombre=data["nombre"],apellido=data["apellido"],desempleado=data["desempleado"])
            cerrajero.save()
            return redirect("index")
            
    form = CerrajeroFormulario()
    return render (request,"profesionales/crear_cerrajero.html ", {'form': form})


def crear_futbolista(request):
    
    if request.method == "POST":
        form = FutbolistaFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            futbolista = Futbolista(nombre=data["nombre"],apellido=data["apellido"],club=data["club"])
            futbolista.save()
            return redirect("index")
            
    form = FutbolistaFormulario()
    return render (request,"profesionales/crear_futbolista.html ", {'form': form})


def crear_profesor(request):
    
    if request.method == "POST":
        form = ProfesorFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            profesor = Profesor(nombre=data["nombre"],apellido=data["apellido"],curso=data["curso"])
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

