from django.contrib import admin

from profesionales.models import Cerrajero, Futbolista, Profesor

# Register your models here.

admin.site.register(Cerrajero)
admin.site.register(Futbolista)
admin.site.register(Profesor)