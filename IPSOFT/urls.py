"""
URL configuration for IPSOFT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



# Uncomment the next two lines to enable the admin:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Farmacia.urls')),
    path('', include('historia_clinica.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('uciapp/',include('uciapp.urls')),
    path('', include('admision.urls')),
    path('notas_enfermeria/', include ('notas_enfermeria.urls')),
    path('Triage', include ('Triage.urls')),


]
