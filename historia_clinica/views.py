from django.shortcuts import get_object_or_404, render, redirect
from .models import Historia_Clinica,Paciente,Genero,Motivo_Consulta,Medico,Enfermeria

import datetime

from.forms import PacienteForm, MedicoForm, EnfermeriaForm

# Create your views here.
def ingresar_paciente(request):
    
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a patient list view
    else:
        # Generate the history number for the new patient
        today = datetime.datetime.now().now().strftime('%d%m%Y')
        last_paciente = Paciente.objects.all().order_by('id').last()
        if last_paciente:
            new_id = last_paciente.id + 1
        else:
            new_id = 1
        historia_clinica = f"{today}-{new_id}"
        
        form = PacienteForm(initial={'historia_clinica': historia_clinica})
    return render(request, 'ingresar_paciente.html', {'form': form})



# Personal Medico # 

def lista_medicos(request): 
    medicos = Medico.objects.all() 
    return render(request, 'lista_medicos.html', {'medicos': medicos})

def ingresar_medico(request): 
    if request.method == 'POST': 
        form = MedicoForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('lista_medicos') 
        else: return render(request, 'ingresar_medico.html', {'form': form})
    else: form = MedicoForm() 
    return render(request, 'ingresar_medico.html', {'form': form})

def actualizar_medico(request, medico_id): 
    medico = get_object_or_404(Medico, id=medico_id) 
    if request.method == 'POST': 
        form = MedicoForm(request.POST, instance=medico) 
        if form.is_valid(): 
            form.save() 
            return redirect('lista_medicos') 
        else: form = MedicoForm(instance=medico) 
        return render(request, 'actualizar_medico.html', {'form': form})
    else: form = MedicoForm(instance=medico) 
    return render(request, 'actualizar_medico.html', {'form': form})
    
def eliminar_medico(request, medico_id): 
    medico = get_object_or_404(Medico, id=medico_id) 
    if request.method == 'POST':
        medico.delete() 
        return redirect('lista_medicos') 
    return render(request, 'eliminar_medico.html', {'medico': medico})


# ENFERMERIA #

def lista_enfermeros(request): 
    enfermeros = Enfermeria.objects.all() 
    return render(request, 'lista_enfermeros.html', {'enfermeros': enfermeros})

def ingresar_enfermero(request): 
    if request.method == 'POST': 
        form = EnfermeriaForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('lista_enfermeros') 
        else: return render(request, 'ingresar_enfermero.html', {'form': form})
    else: form = EnfermeriaForm() 
    return render(request, 'ingresar_enfermero.html', {'form': form})

def actualizar_enfermero(request, enfermero_id): 
    enfermero = get_object_or_404(Enfermeria, id=enfermero_id) 
    if request.method == 'POST': 
        form = EnfermeriaForm(request.POST, instance=enfermero) 
        if form.is_valid(): 
            form.save() 
            return redirect('lista_enfermeros') 
    else: form = EnfermeriaForm(instance=enfermero) 
    return render(request, 'actualizar_enfermero.html', {'form': form})
    
    

def eliminar_enfermero(request, enfermero_id): 
    enfermero = get_object_or_404(Enfermeria, id=enfermero_id) 
    if request.method == 'POST':
        enfermero.delete() 
        return redirect('lista_enfermeros') 
    return render(request, 'eliminar_enfermero.html', {'enfermero': enfermero})