from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota, Observacion
from .forms import NotaForm, ObservacionForm
from django.contrib import messages

def registrar(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La nota ha sido registrada exitosamente.')
            return redirect('lista')
    else:
        form = NotaForm()
    return render(request, 'app/registrar.html', {'form': form})

def lista(request):
    empleados = Nota.objects.all()
    data = {
        'empleados': empleados,
    }
    return render(request, 'app/lista.html', data)
def ver_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    observacion_form = ObservacionForm()

    if request.method == 'POST':
        observacion_form = ObservacionForm(request.POST)
        if observacion_form.is_valid():
            nueva_observacion = observacion_form.save(commit=False)
            nueva_observacion.nota = nota  # Vincula la observación a la nota
            nueva_observacion.save()
            messages.success(request, 'Observación añadida exitosamente.')
            return redirect('ver_nota', id=id)

    return render(request, 'app/ver.html', {
        'nota': nota,
        'observacion_form': observacion_form,
        'observaciones': nota.observaciones.all(),  # Asegúrate de que esto funcione
    })


def actualizar(request, id):
    empleado = get_object_or_404(Nota, id=id)
    if request.method == "POST":
        empleado.nota_enfermeria = request.POST.get('nota_enfermeria')
        empleado.save()
        return redirect('lista')
    return render(request, 'app/actualizar.html', {'no': empleado})

def eliminar(request, id):
    nos = get_object_or_404(Nota, id=id)

    if request.method == 'POST':
        nos.delete()
        messages.success(request, 'La nota ha sido eliminada exitosamente.')
        return redirect('lista')

    return render(request, 'app/eliminar.html', {'nos': nos})

def buscador(request):
    query = request.POST.get('buscar')
    empleados = Nota.objects.filter(identificacion__icontains=query)  # Filtrar por identificación
    return render(request, 'app/lista.html', {'empleados': empleados})

def agregar_observacion(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        form = ObservacionForm(request.POST)
        if form.is_valid():
            nueva_observacion = form.save(commit=False)
            nueva_observacion.nota = nota
            nueva_observacion.save()
            messages.success(request, 'Observación añadida exitosamente.')
            return redirect('ver_nota', id=id)
    else:
        form = ObservacionForm()
    
    return render(request, 'app/agregar_observacion.html', {'form': form, 'nota': nota})