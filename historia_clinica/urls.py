from django.urls import path 
from .views import lista_medicos,actualizar_medico,eliminar_medico, ingresar_medico,ingresar_paciente
from .views import lista_enfermeros, ingresar_enfermero, actualizar_enfermero, eliminar_enfermero
# Esta es la lista de URLs que se usarán para la app Farmacia

urlpatterns = [ 
    # Listar y ingresar médicos
    path('medicos/', lista_medicos, name='lista_medicos'),
    path('medicos/ingresar/', ingresar_medico, name='ingresar_medico'),
    path('medicos/actualizar/<int:medico_id>/', actualizar_medico, name='actualizar_medico'), 
    path('medicos/eliminar/<int:medico_id>/', eliminar_medico, name='eliminar_medico'),

    # Listar y ingresar pacientes

    path('ingresar_paciente/', ingresar_paciente, name='ingresar_paciente'),
    
    # Listar y ingresar enfermeros
    path('enfermeros/', lista_enfermeros, name='lista_enfermeros'),
    path('enfermeros/ingresar/', ingresar_enfermero, name='ingresar_enfermero'),
    path('enfermeros/actualizar/<int:enfermero_id>/', actualizar_enfermero, name='actualizar_enfermero'),
    path('enfermeros/eliminar/<int:enfermero_id>/', eliminar_enfermero, name='eliminar_enfermero'),

]