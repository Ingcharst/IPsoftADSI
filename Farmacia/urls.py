from django.urls import path 
from .views import lista_recetas, index, lista_medicamentos, historial_clinico, atencion_medica, entregar_receta
from .views import lista_recetas_pendientes, lista_recetas_entregadas, detalle_paciente, detalle_paciente_suministrado, lista_pacientes_pendientes
from .views import iniciar_sesion, registro, inicio
from django.contrib.auth.views import LogoutView


urlpatterns = [ 
    path ('',inicio, name="inicio"),
    path('index', index, name="index"),
    path('recetas/', lista_recetas, name='lista_recetas'), 
    path('medicamentos/', lista_medicamentos, name='lista_medicamentos'),
    path('historial/<int:paciente_id>/', historial_clinico, name='historial_clinico'),
    path('atencion_medica/', atencion_medica, name='atencion_medica'),
    path('lista_recetas_pendientes/', lista_recetas_pendientes, name='lista_recetas_pendientes'),
    path('lista_recetas_entregadas/', lista_recetas_entregadas, name='lista_recetas_entregadas'),
    path('paciente/<int:paciente_id>/', detalle_paciente, name='detalle_paciente'),
    path('paciente_suministrado/<int:paciente_id>/', detalle_paciente_suministrado, name='detalle_paciente_suministrado'),
    path('lista_pacientes_pendientes/', lista_pacientes_pendientes, name='lista_pacientes_pendientes'),
 
    path('entregar_receta/<int:receta_id>/', entregar_receta, name='entregar_receta'),


    path('login/', iniciar_sesion, name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', registro, name='register'),
    
    
    ]