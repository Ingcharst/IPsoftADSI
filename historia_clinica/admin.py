from django.contrib import admin

# Register your models here.

from .models import Genero, Historia_Clinica, Motivo_Consulta, Paciente, Medico, Enfermeria

admin.site.register(Historia_Clinica)

admin.site.register(Motivo_Consulta)

admin.site.register(Genero)

admin.site.register(Paciente) 

admin.site.register(Medico)

admin.site.register(Enfermeria)