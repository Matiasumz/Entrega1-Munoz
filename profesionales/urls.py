
from django.urls import path
from . import views

urlpatterns = [
    path("cerrajeros/",views.lista_cerrajeros,name= "cerrajeros"),
    path("cerrajeros/crear/",views.crear_cerrajero, name= "crear_cerrajero"),
    path("futbolistas/",views.lista_futbolistas,name= "futbolistas"),
    path("futbolistas/crear/",views.crear_futbolista, name= "crear_futbolista"),
    path("profesores/",views.lista_profesores,name= "profesores"),
    path("profesor/crear/",views.crear_profesor, name= "crear_profesor"),
    
    #path("",name= "crear_profesor")
]
