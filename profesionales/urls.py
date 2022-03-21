
from django.urls import path
from . import views

urlpatterns = [
    path("cerrajero/crear/",views.crear_cerrajero, name= "crear_cerrajero"),
    path("futbolista/crear/",views.crear_futbolista, name= "crear_futbolista"),
    path("profesor/crear/",views.crear_profesor, name= "crear_profesor"),
    path("cerrajeros/",views.lista_cerrajeros,name= "lista_cerrajeros"),
    path("futbolistas/",views.lista_futbolistas,name= "lista_futbolistas"),
    path("profesores/",views.lista_profesores,name= "lista_profesores"),
    
    #path("",name= "crear_profesor")
]
