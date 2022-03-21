from django.shortcuts import redirect, render


from .forms import CerrajeroFormulario
from .models import Cerrajero

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

