from django.shortcuts import render
from django.http import JsonResponse
import random
from .models import SignosVitales


# Create your views here.

def monitor(request):
    try:
        signos_vitales = SignosVitales.objects.latest('fecha_creacion')
    except SignosVitales.DoesNotExist:
        signos_vitales = SignosVitales(frecuencia_cardiaca=75, 
                                      tension_arterial_sistolica=120, 
                                      tension_arterial_diastolica=80, 
                                      saturacion_oxigeno=98, 
                                      frecuencia_respiratoria=12,
                                      temperatura=37.0)
        signos_vitales.save()

    signos_vitales.simular_signos()
    signos_vitales.save()

    context = {
        'signos_vitales': signos_vitales,
    }

    return render(request, 'uciapp/monitor.html', context)

def activar_urgencia(request):
    # Simula una urgencia
    signos_vitales = SignosVitales.objects.latest('fecha_creacion')
    signos_vitales.urgencia = True
    signos_vitales.simular_signos()
    signos_vitales.save()
    
    return JsonResponse({'status': 'urgencia activada', 'signos': str(signos_vitales)})


"""
def monitor(request):
    vital = SignosVitales.objects.get_or_create(id=1)
    return render(request, 'uciapp/monitor.html', {'vital': vital})


def valores(request):
    vitales = SignosVitales.objects.get(id=1)
    data = {
        "fc": vitales.fc,
        "ta": vitales.ta,
        "pox": vitales.pox,
    }
    return JsonResponse(data)

def emergencia(request):
    vitals = SignosVitales.objects.get(id=1)
    vitals.fc = random.randint(120, 180)
    vitals.ta = f"{random.randint(160, 200)}/{random.randint(100, 120)}"
    vitals.pox = random.randint(85, 92) 
    vitals.save()
    return JsonResponse({"Estado": "emergencia"})
"""