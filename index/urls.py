from django.urls import path
from .views import index , plantilla ,about


urlpatterns = [
    path("",index, name="index"),
    path("about/",about, name="about"),
    path("plantilla/",plantilla,name="plantilla"),
]
