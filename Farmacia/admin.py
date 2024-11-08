from django.contrib import admin

# Register your models here.
from .models import Medicamento, Receta

admin.site.register(Medicamento) 

admin.site.register(Receta)

