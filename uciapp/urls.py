# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('monitor/', views.monitor, name='monitor'),
    path('activar_urgencia/', views.activar_urgencia, name='activar_urgencia'),
    #    path('signos/', views.valores, name='valores'),
#    path('simulador/', views.emergencia, name='emergencia'),
]
