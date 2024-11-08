
from django.urls import path 
from . import views 



urlpatterns = [ 
    path('registrar/', views.registrar, name='registrar'), 
    path('lista/', views.lista, name='lista'), 
    path('ver/<int:id>/', views.ver_nota, name='ver_nota'), 
    path('actualizar/<int:id>/', views.actualizar, name='actualizar'), 
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'), 
    path('buscar/', views.buscador, name='buscador'), 
    path('agregar_observacion/<int:id>/', views.agregar_observacion, name='agregar_observacion'), 
   
    ]