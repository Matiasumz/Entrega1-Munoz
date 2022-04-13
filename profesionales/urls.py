
from django.urls import path
from . import views

urlpatterns = [
    path("cerrajeros/",views.lista_cerrajeros,name= "cerrajeros"),
    path("cerrajeros/crear/",views.crear_cerrajero, name= "crear_cerrajero"),
    path("cerrajeros/<int:pk>/",views.DetalleCerrajero.as_view(), name= "detalle_cerrajero"),
    path("cerrajeros/<int:pk>/editar",views.EditarCerrajero.as_view(), name= "editar_cerrajero"),
    path("cerrajeros/<int:pk>/borrar",views.BorrarCerrajero.as_view(), name= "borrar_cerrajero"),
    path("futbolistas/",views.lista_futbolistas,name= "futbolistas"),
    path("futbolistas/crear/",views.crear_futbolista, name= "crear_futbolista"),
    path("futbolistas/<int:pk>/",views.DetalleFutbolista.as_view(), name= "detalle_futbolista"),
    path("futbolistas/<int:pk>/editar/",views.EditarFutbolista.as_view(), name= "editar_futbolista"),
    path("futbolistas/<int:pk>/borrar/",views.BorrarFutbolista.as_view(), name= "borrar_futbolista"),
    path("profesores/",views.lista_profesores,name= "profesores"),
    path("profesor/crear/",views.crear_profesor, name= "crear_profesor"),
    path("profesor/<int:pk>/",views.DetalleProfesor.as_view(), name= "detalle_profesor"),
    path("profesor/<int:pk>/editar/",views.EditarProfesor.as_view(), name= "editar_profesor"),
    path("profesor/<int:pk>/borrar/",views.BorrarProfesor.as_view(), name= "borrar_profesor"),
    
    #path("",name= "crear_profesor")
]
