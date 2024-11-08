from django.urls import path
from Triage.views import triage, registrar_signos_vitales




urlpatterns = [
    path('', triage, name='triage'),
    path('signos_vitales/', registrar_signos_vitales, name='registrar_signos_vitales'),
    
   ]