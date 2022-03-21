
from django.urls import path
from . import views

urlpatterns = [
    path("cerrajero/crear/",views.crear_cerrajero, name= "crear_cerrajero"),
    path("futbolista/crear/",views.crear_futbolista, name= "crear_futbolista"),
    path("profesor/crear/",views.crear_profesor, name= "crear_profesor"),
    path("cerrajero/buscar/",views.lista_cerrajeros,name= "lista_cerrajeros"),
    #path("",name= "crear_profesor")
]
